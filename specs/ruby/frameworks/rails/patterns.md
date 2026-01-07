# Rails Patterns & Best Practices

## Model Design

### Use Strong Parameters

```ruby
class ArticlesController < ApplicationController
  def create
    @article = Article.new(article_params)
    if @article.save
      redirect_to @article
    else
      render :new, status: :unprocessable_entity
    end
  end

  private

  def article_params
    params.require(:article).permit(:title, :content, :status, tag_ids: [])
  end
end
```

### Scopes and Class Methods

```ruby
class Article < ApplicationRecord
  # Scopes for common queries
  scope :published, -> { where(status: 'published').where('published_at <= ?', Time.current) }
  scope :by_author, ->(author) { where(author: author) }
  scope :recent, -> { order(created_at: :desc) }
  scope :featured, -> { where(featured: true).limit(5) }

  # Class method for complex logic
  def self.search(query)
    return all if query.blank?
    where('title ILIKE :q OR content ILIKE :q', q: "%#{query}%")
  end
end

# Usage
Article.published.by_author(user).recent
Article.search(params[:q]).page(params[:page])
```

### Validations and Callbacks

```ruby
class User < ApplicationRecord
  # Validations
  validates :email, presence: true, uniqueness: { case_sensitive: false },
                    format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :username, presence: true, length: { in: 3..30 },
                       format: { with: /\A[a-z0-9_]+\z/i }

  # Callbacks (use sparingly)
  before_validation :normalize_email
  after_create :send_welcome_email

  private

  def normalize_email
    self.email = email.downcase.strip if email.present?
  end

  def send_welcome_email
    UserMailer.welcome(self).deliver_later
  end
end
```

### Service Objects for Complex Operations

```ruby
# app/services/order_processor.rb
class OrderProcessor
  def initialize(order)
    @order = order
  end

  def call
    return failure('Order already processed') if @order.processed?

    ActiveRecord::Base.transaction do
      charge_payment
      update_inventory
      send_confirmation
      @order.update!(status: 'completed')
    end

    success
  rescue PaymentError => e
    failure(e.message)
  end

  private

  def charge_payment
    PaymentGateway.charge(@order.total, @order.payment_method)
  end

  def update_inventory
    @order.line_items.each do |item|
      item.product.decrement!(:stock, item.quantity)
    end
  end

  def send_confirmation
    OrderMailer.confirmation(@order).deliver_later
  end

  def success
    OpenStruct.new(success?: true)
  end

  def failure(message)
    OpenStruct.new(success?: false, error: message)
  end
end

# Usage in controller
result = OrderProcessor.new(@order).call
if result.success?
  redirect_to @order
else
  flash[:error] = result.error
  render :show
end
```

## Query Optimization

### Avoid N+1 Queries

```ruby
# BAD - N+1 queries
@articles = Article.all
# In view: article.author.name triggers query per article

# GOOD - Eager loading
@articles = Article.includes(:author, :tags)

# For nested associations
@articles = Article.includes(comments: :user)

# Use joins for filtering
@articles = Article.joins(:author).where(authors: { active: true })

# Preload vs Includes vs Eager_load
Article.preload(:tags)     # Separate query, no conditions on tags
Article.includes(:tags)    # Rails chooses strategy
Article.eager_load(:tags)  # LEFT OUTER JOIN, allows conditions
```

### Use Pluck and Select

```ruby
# BAD - Loads full AR objects
User.all.map(&:email)

# GOOD - Direct database query
User.pluck(:email)

# Select specific columns
User.select(:id, :email, :name).where(active: true)
```

## Controllers

### Keep Controllers Thin

```ruby
class ArticlesController < ApplicationController
  before_action :authenticate_user!, except: [:index, :show]
  before_action :set_article, only: [:show, :edit, :update, :destroy]

  def index
    @articles = Article.published.includes(:author).page(params[:page])
  end

  def create
    @article = current_user.articles.build(article_params)

    if @article.save
      redirect_to @article, notice: 'Article created.'
    else
      render :new, status: :unprocessable_entity
    end
  end

  private

  def set_article
    @article = Article.find(params[:id])
  end

  def article_params
    params.require(:article).permit(:title, :content, :status)
  end
end
```

### Use Concerns for Shared Behavior

```ruby
# app/controllers/concerns/paginatable.rb
module Paginatable
  extend ActiveSupport::Concern

  included do
    helper_method :page_size
  end

  def page_size
    params[:per_page]&.to_i || 20
  end

  def paginate(collection)
    collection.page(params[:page]).per(page_size)
  end
end

# Usage
class ArticlesController < ApplicationController
  include Paginatable

  def index
    @articles = paginate(Article.published)
  end
end
```

## Views

### Use Partials and Helpers

```erb
<%# app/views/articles/_article.html.erb %>
<article class="article" id="<%= dom_id(article) %>">
  <h2><%= link_to article.title, article %></h2>
  <p class="meta">
    By <%= article.author.name %> on <%= l(article.published_at, format: :long) %>
  </p>
  <%= truncate(article.content, length: 200) %>
</article>

<%# Usage %>
<%= render @articles %>
<%= render partial: 'article', collection: @articles, cached: true %>
```

### Presenter/Decorator Pattern

```ruby
# app/presenters/article_presenter.rb
class ArticlePresenter < SimpleDelegator
  def initialize(article, view_context)
    super(article)
    @view = view_context
  end

  def formatted_date
    @view.l(published_at, format: :long) if published_at
  end

  def status_badge
    @view.content_tag(:span, status.humanize, class: "badge badge-#{status}")
  end

  def author_link
    @view.link_to(author.name, author)
  end
end

# Usage in view
<% presenter = ArticlePresenter.new(@article, self) %>
<p><%= presenter.formatted_date %></p>
<%= presenter.status_badge %>
```

## Background Jobs

```ruby
class ProcessOrderJob < ApplicationJob
  queue_as :default
  retry_on ActiveRecord::Deadlocked, wait: 5.seconds, attempts: 3
  discard_on ActiveJob::DeserializationError

  def perform(order_id)
    order = Order.find(order_id)
    OrderProcessor.new(order).call
  end
end

# Enqueue
ProcessOrderJob.perform_later(order.id)
ProcessOrderJob.set(wait: 1.hour).perform_later(order.id)
```

## Anti-Patterns to Avoid

### Don't Use Callbacks for Business Logic

```ruby
# BAD - Hidden side effects
class Order < ApplicationRecord
  after_save :process_payment
  after_save :send_notification
  after_save :update_inventory
end

# GOOD - Explicit in controller/service
class OrdersController < ApplicationController
  def create
    @order = Order.new(order_params)
    if @order.save
      OrderProcessor.new(@order).call
      redirect_to @order
    end
  end
end
```

### Don't Query in Views

```erb
<%# BAD - Queries in view %>
<% Article.published.each do |article| %>
  <%= article.title %>
<% end %>

<%# GOOD - Use instance variable from controller %>
<% @articles.each do |article| %>
  <%= article.title %>
<% end %>
```

### Don't Ignore SQL Injection

```ruby
# BAD - SQL injection vulnerability
Article.where("title = '#{params[:title]}'")

# GOOD - Use parameterized queries
Article.where(title: params[:title])
Article.where("title = ?", params[:title])
Article.where("title = :title", title: params[:title])
```
