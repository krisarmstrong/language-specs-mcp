# FastAPI Patterns & Best Practices

## Application Structure

### Project Layout

```
app/
├── main.py              # App entry point
├── config.py            # Settings management
├── dependencies.py      # Shared dependencies
├── models/              # Pydantic models
│   ├── __init__.py
│   ├── user.py
│   └── item.py
├── routers/             # API routes
│   ├── __init__.py
│   ├── users.py
│   └── items.py
├── services/            # Business logic
│   ├── __init__.py
│   └── user_service.py
├── repositories/        # Data access
│   └── user_repo.py
└── db/                  # Database setup
    └── session.py
```

### Application Factory Pattern

```python
# main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.config import settings
from app.routers import users, items
from app.db.session import init_db, close_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown
    await close_db()

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        lifespan=lifespan,
    )

    app.include_router(users.router, prefix="/users", tags=["users"])
    app.include_router(items.router, prefix="/items", tags=["items"])

    return app

app = create_app()
```

## Pydantic Models

### Request/Response Models

```python
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional

# Base model with common fields
class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=100)

# Create request (input)
class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

# Update request (partial)
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = Field(None, min_length=1, max_length=100)

# Response model (output)
class UserResponse(UserBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}  # For ORM mode

# List response with pagination
class UserListResponse(BaseModel):
    items: list[UserResponse]
    total: int
    page: int
    page_size: int
```

### Validation with Field

```python
from pydantic import BaseModel, Field, field_validator
from typing import Annotated

class Product(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    price: float = Field(..., gt=0, description="Price must be positive")
    quantity: int = Field(default=0, ge=0)
    tags: list[str] = Field(default_factory=list, max_length=10)

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Name cannot be blank")
        return v.strip()

# Using Annotated for reusable constraints
PositiveInt = Annotated[int, Field(gt=0)]
NonEmptyStr = Annotated[str, Field(min_length=1)]
```

## Dependency Injection

### Database Session Dependency

```python
# dependencies.py
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import async_session_maker

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise

# Usage in router
from fastapi import Depends

@router.get("/users/{user_id}")
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
) -> UserResponse:
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

### Authentication Dependency

```python
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await db.get(User, user_id)
    if user is None:
        raise credentials_exception
    return user

# Dependency that requires admin role
async def get_admin_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )
    return current_user
```

### Service Layer Dependencies

```python
# services/user_service.py
from fastapi import Depends
from app.repositories.user_repo import UserRepository

class UserService:
    def __init__(self, repo: UserRepository = Depends()):
        self.repo = repo

    async def create_user(self, data: UserCreate) -> User:
        # Hash password
        hashed = hash_password(data.password)
        return await self.repo.create(
            email=data.email,
            name=data.name,
            hashed_password=hashed,
        )

# Usage
@router.post("/users")
async def create_user(
    data: UserCreate,
    service: UserService = Depends(),
) -> UserResponse:
    return await service.create_user(data)
```

## Error Handling

### Custom Exception Handlers

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

class AppException(Exception):
    def __init__(self, status_code: int, detail: str, error_code: str):
        self.status_code = status_code
        self.detail = detail
        self.error_code = error_code

class NotFoundError(AppException):
    def __init__(self, resource: str, id: int):
        super().__init__(
            status_code=404,
            detail=f"{resource} with id {id} not found",
            error_code="NOT_FOUND",
        )

class ValidationError(AppException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=422,
            detail=detail,
            error_code="VALIDATION_ERROR",
        )

# Register handler
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.error_code,
            "detail": exc.detail,
        },
    )
```

## Background Tasks

### Simple Background Tasks

```python
from fastapi import BackgroundTasks

async def send_welcome_email(email: str, name: str):
    # Async email sending logic
    await email_client.send(
        to=email,
        subject="Welcome!",
        body=f"Hello {name}, welcome to our platform!",
    )

@router.post("/users")
async def create_user(
    data: UserCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
) -> UserResponse:
    user = await create_user_in_db(db, data)
    # Queue background task
    background_tasks.add_task(send_welcome_email, user.email, user.name)
    return user
```

### Using Celery for Heavy Tasks

```python
# tasks.py
from celery import Celery

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task
def process_large_file(file_path: str, user_id: int):
    # Heavy processing
    pass

# In router
@router.post("/upload")
async def upload_file(file: UploadFile):
    path = await save_file(file)
    task = process_large_file.delay(path, current_user.id)
    return {"task_id": task.id}

@router.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    task = celery_app.AsyncResult(task_id)
    return {"status": task.status, "result": task.result}
```

## Response Models and Status Codes

### Explicit Response Configuration

```python
from fastapi import status
from fastapi.responses import JSONResponse

@router.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        409: {"description": "User already exists"},
        422: {"description": "Validation error"},
    },
)
async def create_user(data: UserCreate) -> UserResponse:
    existing = await get_user_by_email(data.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",
        )
    return await create_user_in_db(data)

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    await delete_user_from_db(user_id)
    return None  # 204 No Content
```

## Query Parameters and Pagination

### Pagination Dependency

```python
from fastapi import Query
from dataclasses import dataclass

@dataclass
class PaginationParams:
    page: int = Query(1, ge=1, description="Page number")
    page_size: int = Query(20, ge=1, le=100, description="Items per page")

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size

def get_pagination(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
) -> PaginationParams:
    return PaginationParams(page=page, page_size=page_size)

@router.get("/users")
async def list_users(
    pagination: PaginationParams = Depends(get_pagination),
    search: str = Query(None, min_length=1),
    db: AsyncSession = Depends(get_db),
) -> UserListResponse:
    query = select(User)
    if search:
        query = query.where(User.name.ilike(f"%{search}%"))

    total = await db.scalar(select(func.count()).select_from(query))
    users = await db.scalars(
        query.offset(pagination.offset).limit(pagination.page_size)
    )

    return UserListResponse(
        items=users.all(),
        total=total,
        page=pagination.page,
        page_size=pagination.page_size,
    )
```

## Anti-Patterns to Avoid

### Don't Block the Event Loop

```python
# BAD - Blocking call in async function
@router.get("/data")
async def get_data():
    import time
    time.sleep(5)  # Blocks entire server!
    return {"data": "value"}

# GOOD - Use async sleep or run in thread pool
import asyncio
from fastapi.concurrency import run_in_threadpool

@router.get("/data")
async def get_data():
    await asyncio.sleep(5)  # Non-blocking
    return {"data": "value"}

# For CPU-bound or blocking I/O
@router.get("/heavy")
async def heavy_computation():
    result = await run_in_threadpool(cpu_intensive_function)
    return {"result": result}
```

### Don't Expose Internal Models

```python
# BAD - Exposes ORM model directly
@router.get("/users/{id}")
async def get_user(id: int, db: Session) -> User:  # ORM model
    return db.get(User, id)  # May expose sensitive fields

# GOOD - Use response model
@router.get("/users/{id}", response_model=UserResponse)
async def get_user(id: int, db: Session):
    user = db.get(User, id)
    return user  # FastAPI filters to UserResponse fields
```

### Don't Catch Generic Exceptions Silently

```python
# BAD - Hides real errors
@router.post("/users")
async def create_user(data: UserCreate):
    try:
        return await create_user_in_db(data)
    except Exception:
        raise HTTPException(status_code=500, detail="Error")

# GOOD - Handle specific exceptions
@router.post("/users")
async def create_user(data: UserCreate):
    try:
        return await create_user_in_db(data)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="User already exists")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    # Let unexpected errors propagate for proper logging
```

### Don't Forget Response Model Exclusion

```python
# BAD - Password hash could leak if model changes
class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    # What if someone adds hashed_password to User ORM?

# GOOD - Explicitly define what's included
class UserResponse(BaseModel):
    id: int
    email: str
    name: str

    model_config = {
        "from_attributes": True,
        "extra": "forbid",  # Reject unexpected fields
    }
```
