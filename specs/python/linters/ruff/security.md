# Ruff - Security Rules (S / flake8-bandit)

Security-focused rules from Bandit.

## S101: Use of assert

```python
# BAD - assert is stripped in optimized mode
assert user.is_admin, "Admin required"

# GOOD
if not user.is_admin:
    raise PermissionError("Admin required")
```

**Note:** Allow in tests with per-file-ignores.

## S102: Use of exec

```python
# BAD
exec(user_code)

# GOOD - avoid exec entirely
# If absolutely needed, heavily sandbox
```

## S103: Chmod with permissive mask

```python
# BAD
os.chmod(path, 0o777)

# GOOD
os.chmod(path, 0o600)
```

## S104: Binding to all interfaces

```python
# BAD
socket.bind(("0.0.0.0", 8080))

# GOOD
socket.bind(("127.0.0.1", 8080))
```

## S105-S107: Hardcoded passwords

```python
# BAD
password = "admin123"
secret_key = "supersecret"
api_key = "sk-1234567890"

# GOOD
password = os.environ["PASSWORD"]
secret_key = os.environ["SECRET_KEY"]
api_key = os.environ["API_KEY"]
```

## S108: Hardcoded /tmp path

```python
# BAD
with open("/tmp/data.txt", "w") as f:
    f.write(data)

# GOOD
import tempfile
with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
    f.write(data)
```

## S110: Try-except-pass

```python
# BAD - silently ignores errors
try:
    risky()
except Exception:
    pass

# GOOD
try:
    risky()
except Exception:
    logger.exception("Failed")
```

## S112: Try-except-continue

```python
# BAD - silently continues
for item in items:
    try:
        process(item)
    except Exception:
        continue

# GOOD
for item in items:
    try:
        process(item)
    except Exception:
        logger.exception("Failed to process %s", item)
```

## S113: Request without timeout

```python
# BAD
requests.get(url)

# GOOD
requests.get(url, timeout=10)
```

## S301: Pickle unsafe

```python
# BAD
pickle.loads(user_data)  # arbitrary code execution!

# GOOD - use safer alternatives
json.loads(user_data)
```

## S302: Marshal unsafe

```python
# BAD
marshal.loads(user_data)

# GOOD
json.loads(user_data)
```

## S303-S304: Weak crypto

```python
# BAD
import md5
import sha
hashlib.md5(data)
hashlib.sha1(data)

# GOOD
hashlib.sha256(data)
hashlib.sha3_256(data)
```

## S305: Weak cipher

```python
# BAD
from Crypto.Cipher import DES
cipher = DES.new(key)

# GOOD
from Crypto.Cipher import AES
cipher = AES.new(key, AES.MODE_GCM)
```

## S306: mktemp is insecure

```python
# BAD
tempfile.mktemp()

# GOOD
tempfile.mkstemp()
tempfile.NamedTemporaryFile()
```

## S307: eval is dangerous

```python
# BAD
eval(user_input)

# GOOD - use ast.literal_eval for data
import ast
ast.literal_eval(user_input)

# Or parse specifically
json.loads(user_input)
```

## S308: mark_safe without escaping

```python
# BAD (Django)
mark_safe(user_input)

# GOOD
mark_safe(escape(user_input))
```

## S310: URL open suspicious

```python
# BAD - can be file:// or other schemes
urllib.urlopen(user_url)

# GOOD - validate scheme
if user_url.startswith(("http://", "https://")):
    urllib.urlopen(user_url)
```

## S311: Random not cryptographically secure

```python
# BAD for security
import random
token = random.randint(0, 1000000)

# GOOD
import secrets
token = secrets.token_hex(32)
```

## S312: Telnet insecure

```python
# BAD
telnetlib.Telnet(host)

# GOOD
# Use SSH instead
```

## S314-S321: XML vulnerabilities

```python
# BAD - vulnerable to XXE
xml.etree.ElementTree.parse(user_file)
xml.dom.minidom.parse(user_file)
xml.sax.parse(user_file)

# GOOD - use defusedxml
import defusedxml.ElementTree as ET
ET.parse(user_file)
```

## S324: Insecure hash function

```python
# BAD
hashlib.md5(password.encode())

# GOOD for passwords
import bcrypt
bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# Or
from passlib.hash import argon2
argon2.hash(password)
```

## S501: Request with verify=False

```python
# BAD - no SSL verification
requests.get(url, verify=False)

# GOOD
requests.get(url, verify=True)
requests.get(url)  # verify=True is default
```

## S502: SSL with insecure version

```python
# BAD
ssl.SSLContext(ssl.PROTOCOL_SSLv3)

# GOOD
ssl.create_default_context()
ssl.SSLContext(ssl.PROTOCOL_TLS)
```

## S506: YAML unsafe load

```python
# BAD - arbitrary code execution
yaml.load(user_data)
yaml.load(user_data, Loader=yaml.Loader)

# GOOD
yaml.safe_load(user_data)
```

## S507: SSH no host key verification

```python
# BAD
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# GOOD
client.set_missing_host_key_policy(paramiko.RejectPolicy())
# Or load known hosts
client.load_system_host_keys()
```

## S508-S509: Snmp insecure

```python
# BAD
snmp_community = "public"

# GOOD - use SNMPv3 with auth
```

## S601: Shell injection via parameterized string

```python
# BAD
subprocess.call("ls " + user_dir, shell=True)

# GOOD
subprocess.call(["ls", user_dir])
```

## S602: Shell=True without literal

```python
# BAD
subprocess.call(cmd, shell=True)

# GOOD
subprocess.call(cmd.split())
# Or
subprocess.call(shlex.split(cmd))
```

## S603-S607: Subprocess without full path

```python
# BAD
subprocess.call(["ls"])

# GOOD
subprocess.call(["/bin/ls"])
```

## S608: SQL injection

```python
# BAD
cursor.execute("SELECT * FROM users WHERE id = " + user_id)
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# GOOD
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

## S609: Wildcard injection

```python
# BAD
os.system("rm -rf /tmp/*")  # wildcard expansion

# GOOD
import glob
for f in glob.glob("/tmp/*"):
    os.remove(f)
```

## S612: Logging sensitive info

```python
# BAD
logger.debug(f"Password: {password}")

# GOOD
logger.debug("Password: [REDACTED]")
```

## S701: Jinja2 autoescape off

```python
# BAD
jinja2.Environment(autoescape=False)

# GOOD
jinja2.Environment(autoescape=True)
jinja2.Environment(autoescape=select_autoescape())
```
