# Cryptography Guidelines

Based on OWASP Cryptographic Storage Cheat Sheet.

## General Principles

1. **Don't roll your own crypto** - Use established libraries and algorithms
2. **Use high-level APIs** - Prefer libraries that handle implementation details
3. **Keep secrets out of code** - Use environment variables or secret managers
4. **Rotate keys regularly** - Implement key rotation procedures

## Password Storage

### Recommended Algorithms (in order of preference)

1. **Argon2id** - Memory-hard, resistant to GPU attacks
2. **bcrypt** - Widely supported, well-tested
3. **scrypt** - Memory-hard alternative

Never use: MD5, SHA1, SHA256 (alone), or any unsalted hash for passwords.

### Argon2 (Recommended)

```python
# Python - argon2-cffi
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Recommended parameters for 2024+
ph = PasswordHasher(
    time_cost=3,        # Number of iterations
    memory_cost=65536,  # 64 MB
    parallelism=4,      # Number of threads
    hash_len=32,        # Output length
    salt_len=16,        # Salt length
)

def hash_password(password: str) -> str:
    return ph.hash(password)

def verify_password(password: str, hash: str) -> bool:
    try:
        ph.verify(hash, password)
        return True
    except VerifyMismatchError:
        return False

def needs_rehash(hash: str) -> bool:
    """Check if hash needs updating due to parameter changes"""
    return ph.check_needs_rehash(hash)
```

```rust
// Rust - argon2
use argon2::{
    password_hash::{
        rand_core::OsRng, PasswordHash, PasswordHasher, PasswordVerifier, SaltString,
    },
    Argon2, Params,
};

fn hash_password(password: &str) -> Result<String, argon2::password_hash::Error> {
    let salt = SaltString::generate(&mut OsRng);
    let params = Params::new(65536, 3, 4, Some(32))?;
    let argon2 = Argon2::new(argon2::Algorithm::Argon2id, argon2::Version::V0x13, params);
    let hash = argon2.hash_password(password.as_bytes(), &salt)?;
    Ok(hash.to_string())
}

fn verify_password(password: &str, hash: &str) -> bool {
    let parsed = match PasswordHash::new(hash) {
        Ok(h) => h,
        Err(_) => return false,
    };
    Argon2::default()
        .verify_password(password.as_bytes(), &parsed)
        .is_ok()
}
```

### bcrypt

```python
# Python - bcrypt
import bcrypt

BCRYPT_ROUNDS = 12  # Adjust based on hardware (target ~250ms)

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=BCRYPT_ROUNDS)
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(password: str, hash: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hash.encode('utf-8'))
```

```typescript
// TypeScript - bcrypt
import bcrypt from 'bcrypt'

const BCRYPT_ROUNDS = 12

async function hashPassword(password: string): Promise<string> {
  return bcrypt.hash(password, BCRYPT_ROUNDS)
}

async function verifyPassword(password: string, hash: string): Promise<boolean> {
  return bcrypt.compare(password, hash)
}
```

```go
// Go - bcrypt
import "golang.org/x/crypto/bcrypt"

const bcryptCost = 12

func HashPassword(password string) (string, error) {
    hash, err := bcrypt.GenerateFromPassword([]byte(password), bcryptCost)
    return string(hash), err
}

func VerifyPassword(password, hash string) bool {
    return bcrypt.CompareHashAndPassword([]byte(hash), []byte(password)) == nil
}
```

## Symmetric Encryption

### Use AES-256-GCM (Authenticated Encryption)

```python
# Python - cryptography library
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def encrypt(plaintext: bytes, key: bytes) -> bytes:
    """
    Encrypt with AES-256-GCM.
    Returns: nonce (12 bytes) + ciphertext + tag (16 bytes)
    """
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")

    nonce = os.urandom(12)  # 96-bit nonce
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data=None)
    return nonce + ciphertext

def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    """Decrypt AES-256-GCM ciphertext."""
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")

    nonce = ciphertext[:12]
    actual_ciphertext = ciphertext[12:]
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, actual_ciphertext, associated_data=None)
```

```go
// Go - AES-256-GCM
import (
    "crypto/aes"
    "crypto/cipher"
    "crypto/rand"
    "errors"
    "io"
)

func Encrypt(plaintext, key []byte) ([]byte, error) {
    if len(key) != 32 {
        return nil, errors.New("key must be 32 bytes")
    }

    block, err := aes.NewCipher(key)
    if err != nil {
        return nil, err
    }

    gcm, err := cipher.NewGCM(block)
    if err != nil {
        return nil, err
    }

    nonce := make([]byte, gcm.NonceSize())
    if _, err := io.ReadFull(rand.Reader, nonce); err != nil {
        return nil, err
    }

    // Prepend nonce to ciphertext
    return gcm.Seal(nonce, nonce, plaintext, nil), nil
}

func Decrypt(ciphertext, key []byte) ([]byte, error) {
    if len(key) != 32 {
        return nil, errors.New("key must be 32 bytes")
    }

    block, err := aes.NewCipher(key)
    if err != nil {
        return nil, err
    }

    gcm, err := cipher.NewGCM(block)
    if err != nil {
        return nil, err
    }

    if len(ciphertext) < gcm.NonceSize() {
        return nil, errors.New("ciphertext too short")
    }

    nonce := ciphertext[:gcm.NonceSize()]
    ciphertext = ciphertext[gcm.NonceSize():]

    return gcm.Open(nil, nonce, ciphertext, nil)
}
```

### Key Generation

```python
# Generate cryptographically secure random key
import os

def generate_aes_key() -> bytes:
    return os.urandom(32)  # 256 bits

# Or use secrets module
import secrets

def generate_aes_key() -> bytes:
    return secrets.token_bytes(32)
```

## Hashing (Non-Password Data)

### Use SHA-256 or SHA-3 for Integrity

```python
import hashlib

def hash_data(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

# For even stronger security, use SHA-3
def hash_data_sha3(data: bytes) -> str:
    return hashlib.sha3_256(data).hexdigest()
```

### HMAC for Message Authentication

```python
import hmac
import hashlib

def create_hmac(message: bytes, key: bytes) -> bytes:
    return hmac.new(key, message, hashlib.sha256).digest()

def verify_hmac(message: bytes, key: bytes, signature: bytes) -> bool:
    expected = hmac.new(key, message, hashlib.sha256).digest()
    return hmac.compare_digest(expected, signature)  # Constant-time comparison
```

```go
import (
    "crypto/hmac"
    "crypto/sha256"
)

func CreateHMAC(message, key []byte) []byte {
    h := hmac.New(sha256.New, key)
    h.Write(message)
    return h.Sum(nil)
}

func VerifyHMAC(message, key, signature []byte) bool {
    expected := CreateHMAC(message, key)
    return hmac.Equal(expected, signature) // Constant-time comparison
}
```

## Random Number Generation

### Always Use Cryptographically Secure RNG

```python
# Python
import secrets

# Generate random bytes
random_bytes = secrets.token_bytes(32)

# Generate URL-safe token
token = secrets.token_urlsafe(32)

# Generate hex token
hex_token = secrets.token_hex(32)

# Random integer in range
random_int = secrets.randbelow(100)

# NEVER use random module for security
import random  # NOT for security!
```

```typescript
// TypeScript/Node.js
import crypto from 'crypto'

// Generate random bytes
const randomBytes = crypto.randomBytes(32)

// Generate UUID
const uuid = crypto.randomUUID()

// Generate random integer
function secureRandomInt(max: number): number {
  return crypto.randomInt(max)
}
```

```go
import (
    "crypto/rand"
    "encoding/base64"
    "math/big"
)

func GenerateRandomBytes(n int) ([]byte, error) {
    b := make([]byte, n)
    _, err := rand.Read(b)
    return b, err
}

func GenerateSecureToken(n int) (string, error) {
    b, err := GenerateRandomBytes(n)
    if err != nil {
        return "", err
    }
    return base64.URLEncoding.EncodeToString(b), nil
}

func SecureRandomInt(max int64) (int64, error) {
    n, err := rand.Int(rand.Reader, big.NewInt(max))
    if err != nil {
        return 0, err
    }
    return n.Int64(), nil
}
```

## Key Management

### Store Keys Securely

```python
# Environment variables (minimum)
import os
encryption_key = os.environ["ENCRYPTION_KEY"]

# Better: Use a secret manager
# AWS Secrets Manager
import boto3

def get_secret(secret_name: str) -> str:
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)
    return response['SecretString']

# HashiCorp Vault
import hvac

client = hvac.Client(url='https://vault.example.com')
secret = client.secrets.kv.read_secret_version(path='myapp/encryption-key')
key = secret['data']['data']['key']
```

### Key Derivation (from Password)

```python
# Derive encryption key from password using Argon2
from argon2.low_level import hash_secret_raw, Type

def derive_key(password: str, salt: bytes) -> bytes:
    return hash_secret_raw(
        password.encode('utf-8'),
        salt,
        time_cost=3,
        memory_cost=65536,
        parallelism=4,
        hash_len=32,
        type=Type.ID,
    )
```

## What NOT to Use

### Broken/Weak Algorithms

| Algorithm | Problem | Alternative |
|-----------|---------|-------------|
| MD5 | Broken, collisions found | SHA-256, SHA-3 |
| SHA-1 | Broken, collisions found | SHA-256, SHA-3 |
| DES | 56-bit key, too small | AES-256 |
| 3DES | Slow, 112-bit effective | AES-256 |
| RC4 | Multiple vulnerabilities | AES-GCM, ChaCha20 |
| ECB mode | Patterns visible | GCM, CBC with HMAC |
| CBC without MAC | Padding oracle attacks | GCM (authenticated) |

### Common Mistakes

```python
# BAD - ECB mode shows patterns
cipher = AES.new(key, AES.MODE_ECB)

# BAD - CBC without authentication
cipher = AES.new(key, AES.MODE_CBC, iv)

# BAD - Predictable IV
iv = b'\x00' * 16

# BAD - Using hash for passwords
password_hash = hashlib.sha256(password).hexdigest()

# BAD - Short or predictable keys
key = "password123"

# BAD - Reusing nonces
nonce = b'\x00' * 12  # Same nonce every time
```

## TLS Configuration

```python
# Python - Enforce TLS 1.2+
import ssl
import urllib.request

context = ssl.create_default_context()
context.minimum_version = ssl.TLSVersion.TLSv1_2
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True

# For requests library
import requests
response = requests.get('https://example.com', verify=True)  # verify=True is default
```

```go
// Go - TLS configuration
import (
    "crypto/tls"
    "net/http"
)

client := &http.Client{
    Transport: &http.Transport{
        TLSClientConfig: &tls.Config{
            MinVersion: tls.VersionTLS12,
        },
    },
}
```
