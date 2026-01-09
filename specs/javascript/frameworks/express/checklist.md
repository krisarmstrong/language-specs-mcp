# Express.js Generation Checklist

**Read this BEFORE generating Express/Node.js backend code.**

## Critical Rules

### 1. Always Use Async Error Handling
```javascript
// BAD - Unhandled promise rejection crashes server
app.get('/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id);
  res.json(user);
});

// GOOD - Wrap async routes
const asyncHandler = fn => (req, res, next) =>
  Promise.resolve(fn(req, res, next)).catch(next);

app.get('/users/:id', asyncHandler(async (req, res) => {
  const user = await User.findById(req.params.id);
  res.json(user);
}));

// BETTER - Use express-async-errors
require('express-async-errors');
```

### 2. Validate All Input
```javascript
// BAD - Trust user input
app.post('/users', (req, res) => {
  User.create(req.body);  // Accepts anything!
});

// GOOD - Validate with schema
import { z } from 'zod';

const CreateUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  age: z.number().int().positive().optional()
});

app.post('/users', (req, res) => {
  const data = CreateUserSchema.parse(req.body);
  User.create(data);
});
```

### 3. Parameterized Queries
```javascript
// BAD - SQL injection
const user = await db.query(
  `SELECT * FROM users WHERE id = '${req.params.id}'`
);

// GOOD - Parameterized
const user = await db.query(
  'SELECT * FROM users WHERE id = $1',
  [req.params.id]
);
```

### 4. Set Security Headers
```javascript
// MUST HAVE
import helmet from 'helmet';
app.use(helmet());

// Manual alternative
app.use((req, res, next) => {
  res.setHeader('X-Content-Type-Options', 'nosniff');
  res.setHeader('X-Frame-Options', 'DENY');
  res.setHeader('X-XSS-Protection', '1; mode=block');
  next();
});
```

### 5. Rate Limiting
```javascript
import rateLimit from 'express-rate-limit';

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  standardHeaders: true,
  legacyHeaders: false,
});

app.use('/api/', limiter);

// Stricter for auth endpoints
const authLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 5,
});
app.use('/api/login', authLimiter);
```

### 6. CORS Configuration
```javascript
// BAD - Allow everything
app.use(cors());

// GOOD - Explicit origins
app.use(cors({
  origin: ['https://myapp.com', 'https://admin.myapp.com'],
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
}));
```

### 7. Secure Session/Cookie Settings
```javascript
app.use(session({
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  cookie: {
    secure: process.env.NODE_ENV === 'production', // HTTPS only
    httpOnly: true,      // No JS access
    sameSite: 'strict',  // CSRF protection
    maxAge: 3600000      // 1 hour
  }
}));
```

### 8. Proper Error Handling
```javascript
// Error handler middleware (must be last)
app.use((err, req, res, next) => {
  console.error(err.stack);
  
  // Don't leak error details in production
  if (process.env.NODE_ENV === 'production') {
    res.status(500).json({ error: 'Internal server error' });
  } else {
    res.status(500).json({ error: err.message, stack: err.stack });
  }
});
```

### 9. Request Size Limits
```javascript
// Prevent DoS via large payloads
app.use(express.json({ limit: '10kb' }));
app.use(express.urlencoded({ extended: true, limit: '10kb' }));
```

### 10. Trust Proxy (Behind Load Balancer)
```javascript
// When behind nginx/cloudflare
app.set('trust proxy', 1);

// Then req.ip gives real client IP
```

## Security Checklist
- [ ] helmet() middleware enabled
- [ ] Rate limiting on all routes
- [ ] Input validation on all endpoints
- [ ] Parameterized database queries
- [ ] CORS properly configured
- [ ] Cookies: secure, httpOnly, sameSite
- [ ] No secrets in code (use env vars)
- [ ] Error messages don't leak in production

## Production Checklist
- [ ] NODE_ENV=production
- [ ] Process manager (PM2, systemd)
- [ ] Graceful shutdown handling
- [ ] Health check endpoint
- [ ] Structured logging (pino, winston)
