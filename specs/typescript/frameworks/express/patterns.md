# Express.js Patterns & Best Practices (TypeScript)

## Application Structure

### Project Layout

```
src/
├── index.ts              # Entry point
├── app.ts                # Express app setup
├── config/
│   └── index.ts          # Configuration
├── routes/
│   ├── index.ts          # Route aggregation
│   ├── users.ts
│   └── items.ts
├── controllers/
│   ├── userController.ts
│   └── itemController.ts
├── services/
│   ├── userService.ts
│   └── itemService.ts
├── middleware/
│   ├── auth.ts
│   ├── errorHandler.ts
│   └── validation.ts
├── models/
│   └── User.ts
├── types/
│   └── index.ts
└── utils/
    └── asyncHandler.ts
```

### Application Setup

```typescript
// app.ts
import express, { Express } from 'express'
import helmet from 'helmet'
import cors from 'cors'
import compression from 'compression'

import { config } from './config'
import { errorHandler, notFoundHandler } from './middleware/errorHandler'
import routes from './routes'

export function createApp(): Express {
  const app = express()

  // Security middleware
  app.use(helmet())
  app.use(cors({ origin: config.corsOrigins }))

  // Parsing middleware
  app.use(express.json({ limit: '10kb' }))
  app.use(express.urlencoded({ extended: true }))
  app.use(compression())

  // Routes
  app.use('/api/v1', routes)

  // Error handling (must be last)
  app.use(notFoundHandler)
  app.use(errorHandler)

  return app
}

// index.ts
import { createApp } from './app'
import { config } from './config'

const app = createApp()

app.listen(config.port, () => {
  console.log(`Server running on port ${config.port}`)
})
```

## Type Definitions

### Request Types

```typescript
// types/index.ts
import { Request } from 'express'

export interface AuthenticatedRequest extends Request {
  user: {
    id: string
    email: string
    role: 'user' | 'admin'
  }
}

export interface PaginationQuery {
  page?: string
  limit?: string
  sort?: string
  order?: 'asc' | 'desc'
}

export interface TypedRequest<
  TBody = unknown,
  TQuery = unknown,
  TParams = unknown,
> extends Request {
  body: TBody
  query: TQuery
  params: TParams
}

// Usage
interface CreateUserBody {
  email: string
  name: string
  password: string
}

type CreateUserRequest = TypedRequest<CreateUserBody>
```

## Controllers

### Controller Pattern

```typescript
// controllers/userController.ts
import { Response, NextFunction } from 'express'
import { UserService } from '../services/userService'
import { TypedRequest, AuthenticatedRequest } from '../types'
import { AppError } from '../utils/errors'

const userService = new UserService()

interface CreateUserBody {
  email: string
  name: string
  password: string
}

interface UserParams {
  id: string
}

export const createUser = async (
  req: TypedRequest<CreateUserBody>,
  res: Response,
  next: NextFunction
) => {
  try {
    const user = await userService.create(req.body)
    res.status(201).json({
      status: 'success',
      data: { user },
    })
  } catch (error) {
    next(error)
  }
}

export const getUser = async (
  req: TypedRequest<unknown, unknown, UserParams>,
  res: Response,
  next: NextFunction
) => {
  try {
    const user = await userService.findById(req.params.id)
    if (!user) {
      throw new AppError('User not found', 404)
    }
    res.json({
      status: 'success',
      data: { user },
    })
  } catch (error) {
    next(error)
  }
}

export const getCurrentUser = async (
  req: AuthenticatedRequest,
  res: Response
) => {
  res.json({
    status: 'success',
    data: { user: req.user },
  })
}
```

## Middleware

### Async Handler Wrapper

```typescript
// utils/asyncHandler.ts
import { Request, Response, NextFunction, RequestHandler } from 'express'

type AsyncRequestHandler = (
  req: Request,
  res: Response,
  next: NextFunction
) => Promise<void>

export const asyncHandler =
  (fn: AsyncRequestHandler): RequestHandler =>
  (req, res, next) => {
    Promise.resolve(fn(req, res, next)).catch(next)
  }

// Usage - no try/catch needed
export const getUsers = asyncHandler(async (req, res) => {
  const users = await userService.findAll()
  res.json({ status: 'success', data: { users } })
})
```

### Error Handling Middleware

```typescript
// middleware/errorHandler.ts
import { Request, Response, NextFunction } from 'express'
import { config } from '../config'

export class AppError extends Error {
  constructor(
    message: string,
    public statusCode: number = 500,
    public code?: string
  ) {
    super(message)
    this.name = 'AppError'
    Error.captureStackTrace(this, this.constructor)
  }
}

export const notFoundHandler = (req: Request, res: Response) => {
  res.status(404).json({
    status: 'error',
    message: `Route ${req.originalUrl} not found`,
  })
}

export const errorHandler = (
  err: Error,
  req: Request,
  res: Response,
  _next: NextFunction
) => {
  // Log error for debugging
  console.error('Error:', err)

  if (err instanceof AppError) {
    return res.status(err.statusCode).json({
      status: 'error',
      message: err.message,
      code: err.code,
    })
  }

  // Handle specific error types
  if (err.name === 'ValidationError') {
    return res.status(400).json({
      status: 'error',
      message: err.message,
    })
  }

  if (err.name === 'JsonWebTokenError') {
    return res.status(401).json({
      status: 'error',
      message: 'Invalid token',
    })
  }

  // Generic error (hide details in production)
  res.status(500).json({
    status: 'error',
    message: config.isDev ? err.message : 'Internal server error',
    ...(config.isDev && { stack: err.stack }),
  })
}
```

### Authentication Middleware

```typescript
// middleware/auth.ts
import { Response, NextFunction } from 'express'
import jwt from 'jsonwebtoken'
import { AuthenticatedRequest } from '../types'
import { AppError } from './errorHandler'
import { config } from '../config'

interface TokenPayload {
  id: string
  email: string
  role: 'user' | 'admin'
}

export const authenticate = async (
  req: AuthenticatedRequest,
  res: Response,
  next: NextFunction
) => {
  try {
    const authHeader = req.headers.authorization
    if (!authHeader?.startsWith('Bearer ')) {
      throw new AppError('No token provided', 401)
    }

    const token = authHeader.substring(7)
    const payload = jwt.verify(token, config.jwtSecret) as TokenPayload

    req.user = {
      id: payload.id,
      email: payload.email,
      role: payload.role,
    }

    next()
  } catch (error) {
    if (error instanceof jwt.JsonWebTokenError) {
      next(new AppError('Invalid token', 401))
    } else {
      next(error)
    }
  }
}

export const requireRole =
  (...roles: string[]) =>
  (req: AuthenticatedRequest, res: Response, next: NextFunction) => {
    if (!roles.includes(req.user.role)) {
      return next(new AppError('Insufficient permissions', 403))
    }
    next()
  }
```

### Validation Middleware

```typescript
// middleware/validation.ts
import { Request, Response, NextFunction } from 'express'
import { z, ZodSchema } from 'zod'
import { AppError } from './errorHandler'

export const validate =
  (schema: ZodSchema, source: 'body' | 'query' | 'params' = 'body') =>
  (req: Request, res: Response, next: NextFunction) => {
    try {
      const result = schema.safeParse(req[source])
      if (!result.success) {
        const errors = result.error.errors.map((e) => ({
          field: e.path.join('.'),
          message: e.message,
        }))
        throw new AppError('Validation failed', 400)
      }
      req[source] = result.data
      next()
    } catch (error) {
      next(error)
    }
  }

// Schemas
export const createUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  password: z.string().min(8),
})

export const paginationSchema = z.object({
  page: z.coerce.number().int().positive().default(1),
  limit: z.coerce.number().int().min(1).max(100).default(20),
})

// Usage in routes
router.post('/users', validate(createUserSchema), createUser)
router.get('/users', validate(paginationSchema, 'query'), getUsers)
```

## Routes

### Route Organization

```typescript
// routes/index.ts
import { Router } from 'express'
import userRoutes from './users'
import itemRoutes from './items'
import authRoutes from './auth'

const router = Router()

router.use('/auth', authRoutes)
router.use('/users', userRoutes)
router.use('/items', itemRoutes)

export default router

// routes/users.ts
import { Router } from 'express'
import { authenticate, requireRole } from '../middleware/auth'
import { validate } from '../middleware/validation'
import { asyncHandler } from '../utils/asyncHandler'
import * as userController from '../controllers/userController'
import { createUserSchema, updateUserSchema } from '../schemas/user'

const router = Router()

// Public routes
router.post(
  '/',
  validate(createUserSchema),
  asyncHandler(userController.createUser)
)

// Protected routes
router.use(authenticate) // All routes below require auth

router.get('/me', asyncHandler(userController.getCurrentUser))
router.get('/:id', asyncHandler(userController.getUser))
router.patch(
  '/:id',
  validate(updateUserSchema),
  asyncHandler(userController.updateUser)
)

// Admin only
router.delete(
  '/:id',
  requireRole('admin'),
  asyncHandler(userController.deleteUser)
)

export default router
```

## Response Patterns

### Consistent Response Format

```typescript
// utils/response.ts
import { Response } from 'express'

interface SuccessResponse<T> {
  status: 'success'
  data: T
  meta?: {
    page?: number
    limit?: number
    total?: number
  }
}

interface ErrorResponse {
  status: 'error'
  message: string
  code?: string
  errors?: Array<{ field: string; message: string }>
}

export const sendSuccess = <T>(
  res: Response,
  data: T,
  statusCode = 200,
  meta?: SuccessResponse<T>['meta']
) => {
  const response: SuccessResponse<T> = { status: 'success', data }
  if (meta) response.meta = meta
  res.status(statusCode).json(response)
}

export const sendPaginated = <T>(
  res: Response,
  items: T[],
  { page, limit, total }: { page: number; limit: number; total: number }
) => {
  sendSuccess(res, { items }, 200, { page, limit, total })
}

// Usage
export const getUsers = asyncHandler(async (req, res) => {
  const { page, limit } = req.query
  const { users, total } = await userService.findPaginated(page, limit)
  sendPaginated(res, users, { page, limit, total })
})
```

## Anti-Patterns to Avoid

### Don't Use Callbacks for Async Operations

```typescript
// BAD - Callback style, error-prone
router.get('/users', (req, res) => {
  db.query('SELECT * FROM users', (err, results) => {
    if (err) {
      res.status(500).json({ error: err.message })
      return
    }
    res.json(results)
  })
})

// GOOD - Async/await with error handling
router.get(
  '/users',
  asyncHandler(async (req, res) => {
    const users = await db.query('SELECT * FROM users')
    res.json({ status: 'success', data: { users } })
  })
)
```

### Don't Forget Error Handling

```typescript
// BAD - Unhandled promise rejection crashes server
router.get('/users/:id', async (req, res) => {
  const user = await userService.findById(req.params.id) // May throw!
  res.json(user)
})

// GOOD - Proper error handling
router.get(
  '/users/:id',
  asyncHandler(async (req, res) => {
    const user = await userService.findById(req.params.id)
    if (!user) {
      throw new AppError('User not found', 404)
    }
    res.json({ status: 'success', data: { user } })
  })
)
```

### Don't Trust User Input

```typescript
// BAD - SQL injection vulnerability
router.get('/users', async (req, res) => {
  const { search } = req.query
  const users = await db.query(`SELECT * FROM users WHERE name = '${search}'`)
  res.json(users)
})

// GOOD - Parameterized queries
router.get('/users', async (req, res) => {
  const { search } = req.query
  const users = await db.query('SELECT * FROM users WHERE name = $1', [search])
  res.json({ status: 'success', data: { users } })
})
```

### Don't Block the Event Loop

```typescript
// BAD - Synchronous file read blocks server
router.get('/file', (req, res) => {
  const data = fs.readFileSync('/large-file.json') // Blocks!
  res.json(JSON.parse(data.toString()))
})

// GOOD - Async operations
router.get(
  '/file',
  asyncHandler(async (req, res) => {
    const data = await fs.promises.readFile('/large-file.json')
    res.json(JSON.parse(data.toString()))
  })
)

// For CPU-intensive work, use worker threads
import { Worker } from 'worker_threads'

router.get(
  '/heavy',
  asyncHandler(async (req, res) => {
    const result = await runInWorker('./heavy-task.js', req.body)
    res.json({ status: 'success', data: { result } })
  })
)
```

### Don't Expose Sensitive Information

```typescript
// BAD - Leaks internal details
app.use((err, req, res, next) => {
  res.status(500).json({
    error: err.message,
    stack: err.stack, // Never in production!
    query: req.query, // User data exposure
  })
})

// GOOD - Safe error responses
app.use((err, req, res, next) => {
  const statusCode = err.statusCode || 500
  res.status(statusCode).json({
    status: 'error',
    message: statusCode === 500 ? 'Internal server error' : err.message,
  })
})
```

### Don't Mix Business Logic in Routes

```typescript
// BAD - Business logic in route handler
router.post('/orders', async (req, res) => {
  const { items, userId } = req.body
  // All logic crammed here
  const total = items.reduce((sum, item) => sum + item.price * item.qty, 0)
  if (total > 10000) {
    // Apply discount
  }
  const order = await db.insert('orders', { userId, items, total })
  await sendEmail(userId, 'Order confirmation', order)
  res.json(order)
})

// GOOD - Delegate to service layer
router.post(
  '/orders',
  asyncHandler(async (req, res) => {
    const order = await orderService.create(req.body)
    sendSuccess(res, { order }, 201)
  })
)

// services/orderService.ts
class OrderService {
  async create(data: CreateOrderInput): Promise<Order> {
    const total = this.calculateTotal(data.items)
    const finalTotal = this.applyDiscounts(total)
    const order = await this.orderRepo.create({ ...data, total: finalTotal })
    await this.notificationService.sendOrderConfirmation(order)
    return order
  }
}
```
