# FastAPI Generation Checklist

**Read this BEFORE generating FastAPI code.**

## Critical Rules

### 1. Use Pydantic for All Input
```python
# BAD - No validation
@app.post("/users")
async def create_user(data: dict):
    return User.create(**data)

# GOOD - Validated model
from pydantic import BaseModel, EmailStr, Field

class CreateUserRequest(BaseModel):
    email: EmailStr
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(gt=0, lt=150)

@app.post("/users")
async def create_user(data: CreateUserRequest):
    return User.create(**data.model_dump())
```

### 2. Dependency Injection for Auth
```python
# BAD - Check auth in every endpoint
@app.get("/users/{user_id}")
async def get_user(user_id: int, token: str = Header()):
    user = verify_token(token)
    if not user:
        raise HTTPException(401)
    ...

# GOOD - Reusable dependency
async def get_current_user(
    token: str = Depends(oauth2_scheme)
) -> User:
    user = verify_token(token)
    if not user:
        raise HTTPException(401, "Invalid token")
    return user

@app.get("/users/{user_id}")
async def get_user(
    user_id: int,
    current_user: User = Depends(get_current_user)
):
    ...
```

### 3. Always Check Authorization
```python
# BAD - Only checks authentication
@app.get("/users/{user_id}/data")
async def get_user_data(
    user_id: int,
    current_user: User = Depends(get_current_user)
):
    return await fetch_data(user_id)  # Anyone can access any user!

# GOOD - Checks authorization too
@app.get("/users/{user_id}/data")
async def get_user_data(
    user_id: int,
    current_user: User = Depends(get_current_user)
):
    if current_user.id != user_id and not current_user.is_admin:
        raise HTTPException(403, "Access denied")
    return await fetch_data(user_id)
```

### 4. Async Database Operations
```python
# BAD - Blocking call in async function
@app.get("/users")
async def list_users():
    return db.query(User).all()  # Blocks event loop!

# GOOD - Async ORM
from sqlalchemy.ext.asyncio import AsyncSession

@app.get("/users")
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    return result.scalars().all()
```

### 5. Proper Exception Handling
```python
# BAD - Leaks internal errors
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return await db.get(User, user_id)  # Returns None or crashes

# GOOD - Explicit error handling
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(404, f"User {user_id} not found")
    return user
```

### 6. Background Tasks for Slow Operations
```python
# BAD - Blocks response
@app.post("/reports")
async def create_report(data: ReportRequest):
    report = generate_report(data)  # Takes 30 seconds
    send_email(report)              # Takes 5 seconds
    return {"status": "done"}

# GOOD - Background task
from fastapi import BackgroundTasks

@app.post("/reports")
async def create_report(
    data: ReportRequest,
    background_tasks: BackgroundTasks
):
    report_id = create_report_record(data)
    background_tasks.add_task(generate_and_send_report, report_id)
    return {"status": "processing", "report_id": report_id}
```

### 7. Response Model for Output Validation
```python
# BAD - May expose internal fields
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return await db.get(User, user_id)  # Includes password_hash!

# GOOD - Explicit response model
class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    # password_hash not included

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    return await db.get(User, user_id)
```

### 8. Rate Limiting
```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/login")
@limiter.limit("5/minute")
async def login(request: Request, credentials: LoginRequest):
    ...
```

### 9. CORS Configuration
```python
# BAD - Allow everything
app.add_middleware(CORSMiddleware, allow_origins=["*"])

# GOOD - Explicit origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://myapp.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
```

### 10. Secure Settings Pattern
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    
    class Config:
        env_file = ".env"

settings = Settings()

# Usage
if settings.debug:
    ...
```

## Security Checklist
- [ ] All input validated with Pydantic
- [ ] Auth via dependencies, not manual checks
- [ ] Authorization checked (not just authentication)
- [ ] Response models hide sensitive fields
- [ ] Rate limiting on sensitive endpoints
- [ ] CORS properly configured
- [ ] Secrets from environment variables

## Performance Checklist
- [ ] Async database driver
- [ ] Background tasks for slow operations
- [ ] Connection pooling configured
- [ ] Response compression enabled
