# Django Generation Checklist

**Read this BEFORE generating Django code.**

## Critical Rules

### 1. Never Use raw() with User Input
```python
# VULNERABLE - SQL injection
User.objects.raw(f"SELECT * FROM users WHERE name = '{name}'")

# SAFE - Parameterized
User.objects.raw("SELECT * FROM users WHERE name = %s", [name])

# BETTER - Use ORM
User.objects.filter(name=name)
```

### 2. Use Django's ORM Methods
```python
# BAD - Manual and error-prone
user = User.objects.filter(id=user_id)
if user:
    user = user[0]
else:
    raise Http404

# GOOD - Built-in shortcut
from django.shortcuts import get_object_or_404
user = get_object_or_404(User, id=user_id)
```

### 3. CSRF Protection
```python
# REQUIRED in templates for POST forms
<form method="post">
    {% csrf_token %}
    ...
</form>

# For AJAX, include token in headers
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
fetch(url, {
    method: 'POST',
    headers: {'X-CSRFToken': csrftoken},
    ...
});

# NEVER do this
@csrf_exempt  # Only for webhooks with other auth
def my_view(request):
    ...
```

### 4. User Input in Templates is Auto-Escaped
```html
<!-- SAFE - Auto-escaped -->
<p>{{ user_input }}</p>

<!-- DANGEROUS - Only if you sanitized the content -->
<p>{{ user_input|safe }}</p>

<!-- NEVER with user content -->
{% autoescape off %}{{ user_html }}{% endautoescape %}
```

### 5. Check Object Permissions
```python
# BAD - Only checks authentication
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Anyone can edit any post!

# GOOD - Checks ownership
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        raise PermissionDenied
    ...

# BETTER - Use django-guardian or similar
from guardian.decorators import permission_required_or_403

@permission_required_or_403('posts.change_post', (Post, 'id', 'post_id'))
def edit_post(request, post_id):
    ...
```

### 6. Form Validation
```python
# BAD - Direct model creation
def create_user(request):
    User.objects.create(
        email=request.POST['email'],
        name=request.POST['name']
    )

# GOOD - Form validation
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name']

def create_user(request):
    form = UserForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        return render(request, 'form.html', {'form': form})
```

### 7. File Upload Security
```python
# settings.py
MEDIA_ROOT = BASE_DIR / 'media'
DATA_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024  # 5MB

# models.py
from django.core.validators import FileExtensionValidator

class Document(models.Model):
    file = models.FileField(
        upload_to='documents/',
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])]
    )
```

### 8. Secure Settings for Production
```python
# settings.py
DEBUG = False  # CRITICAL
ALLOWED_HOSTS = ['myapp.com', 'www.myapp.com']

# Security middleware (enabled by default, verify present)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    ...
]

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

### 9. Secret Key Management
```python
# BAD
SECRET_KEY = 'my-secret-key-here'

# GOOD
import os
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Or use django-environ
import environ
env = environ.Env()
SECRET_KEY = env('SECRET_KEY')
```

### 10. Database Query Optimization
```python
# BAD - N+1 queries
posts = Post.objects.all()
for post in posts:
    print(post.author.name)  # Query per post!

# GOOD - Eager loading
posts = Post.objects.select_related('author').all()
for post in posts:
    print(post.author.name)  # No extra queries

# For many-to-many
posts = Post.objects.prefetch_related('tags').all()
```

## Security Checklist
- [ ] DEBUG = False in production
- [ ] SECRET_KEY from environment
- [ ] ALLOWED_HOSTS configured
- [ ] CSRF protection enabled
- [ ] SSL/HTTPS enforced
- [ ] Security headers enabled
- [ ] File uploads validated
- [ ] Object-level permissions checked

## Common Mistakes
- [ ] Using .filter() when you need .get() (or vice versa)
- [ ] Forgetting to call .save() after modifying model
- [ ] Not using transactions for related operations
- [ ] Exposing sensitive fields in serializers
- [ ] Not paginating large querysets
