# Django Patterns & Best Practices

## Model Design

### Use Proper Field Types

```python
from django.db import models
from django.utils import timezone

class Article(models.Model):
    # GOOD - Proper field choices
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()

    # Use choices for constrained values
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', 'published_at']),
        ]
```

### Model Methods over Business Logic in Views

```python
class Order(models.Model):
    status = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    # GOOD - Business logic in model
    def can_be_cancelled(self) -> bool:
        return self.status in ('pending', 'confirmed')

    def cancel(self) -> None:
        if not self.can_be_cancelled():
            raise ValueError("Order cannot be cancelled")
        self.status = 'cancelled'
        self.save(update_fields=['status'])

    @property
    def is_paid(self) -> bool:
        return self.status == 'paid'
```

### Custom Managers and QuerySets

```python
class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(
            status='published',
            published_at__lte=timezone.now()
        )

    def by_author(self, author):
        return self.filter(author=author)

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

class Article(models.Model):
    objects = ArticleManager()

# Usage
Article.objects.published().by_author(user)
```

## Views

### Class-Based Views

```python
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = 'articles'
    paginate_by = 20

    def get_queryset(self):
        return Article.objects.published().select_related('author')

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```

### API Views with DRF

```python
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == 'list':
            queryset = queryset.published()
        return queryset.select_related('author')

    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        article = self.get_object()
        article.publish()
        return Response({'status': 'published'})
```

## Query Optimization

### Avoid N+1 Queries

```python
# BAD - N+1 queries
articles = Article.objects.all()
for article in articles:
    print(article.author.name)  # Query per article!

# GOOD - select_related for ForeignKey
articles = Article.objects.select_related('author').all()

# GOOD - prefetch_related for ManyToMany
articles = Article.objects.prefetch_related('tags', 'comments').all()

# Prefetch with custom queryset
from django.db.models import Prefetch

articles = Article.objects.prefetch_related(
    Prefetch(
        'comments',
        queryset=Comment.objects.filter(approved=True).order_by('-created_at')[:5]
    )
)
```

### Use F() and Q() Objects

```python
from django.db.models import F, Q

# F() for database-level operations
Article.objects.update(views=F('views') + 1)

# Avoid race conditions
article.views = F('views') + 1
article.save(update_fields=['views'])

# Q() for complex queries
Article.objects.filter(
    Q(status='published') | Q(author=user),
    created_at__gte=last_week
)
```

## Security

### Always Use CSRF Protection

```python
# Template
<form method="post">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Submit</button>
</form>

# AJAX with CSRF
// Get token from cookie
const csrftoken = document.cookie.match(/csrftoken=([^;]+)/)?.[1];
fetch('/api/endpoint/', {
    method: 'POST',
    headers: {
        'X-CSRFToken': csrftoken,
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
});
```

### Validate and Sanitize Input

```python
from django import forms
from django.core.validators import MinLengthValidator

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        validators=[MinLengthValidator(5)],
        strip=True  # Remove leading/trailing whitespace
    )

    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data['title']
        if Article.objects.filter(title__iexact=title).exists():
            raise forms.ValidationError("Article with this title exists")
        return title
```

## Anti-Patterns to Avoid

### Don't Put Logic in Templates

```django
{# BAD - Logic in template #}
{% for article in articles %}
    {% if article.status == 'published' and article.published_at <= now %}
        {{ article.title }}
    {% endif %}
{% endfor %}

{# GOOD - Filter in view #}
{% for article in published_articles %}
    {{ article.title }}
{% endfor %}
```

### Don't Ignore Database Transactions

```python
from django.db import transaction

# BAD - Partial failures possible
def transfer_funds(from_account, to_account, amount):
    from_account.balance -= amount
    from_account.save()
    # If this fails, money is lost!
    to_account.balance += amount
    to_account.save()

# GOOD - Atomic transaction
@transaction.atomic
def transfer_funds(from_account, to_account, amount):
    from_account.balance -= amount
    from_account.save()
    to_account.balance += amount
    to_account.save()
```

### Don't Hardcode URLs

```python
# BAD
redirect('/articles/1/')

# GOOD
from django.urls import reverse
redirect(reverse('article-detail', kwargs={'pk': 1}))

# In templates
<a href="{% url 'article-detail' pk=article.pk %}">View</a>
```
