# Dockerfile Generation Checklist

**Read this BEFORE writing Dockerfiles. Security and image size matter.**

## Critical: You Must Do These

### 1. Use Specific Base Image Tags
```dockerfile
# BAD - unpredictable, changes over time
FROM node
FROM python
FROM ubuntu:latest

# GOOD - pinned versions
FROM node:20.10-alpine
FROM python:3.12-slim
FROM ubuntu:22.04
```

### 2. Don't Run as Root
```dockerfile
# BAD - runs as root
FROM node:20-alpine
COPY . .
CMD ["node", "app.js"]

# GOOD - create and use non-root user
FROM node:20-alpine
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
WORKDIR /app
COPY --chown=appuser:appgroup . .
USER appuser
CMD ["node", "app.js"]
```

### 3. Use Multi-Stage Builds
```dockerfile
# BAD - includes build tools in final image
FROM node:20
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
CMD ["node", "dist/app.js"]

# GOOD - multi-stage, smaller final image
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER node
CMD ["node", "dist/app.js"]
```

### 4. Order Layers for Cache Efficiency
```dockerfile
# BAD - invalidates cache on any code change
FROM node:20-alpine
COPY . .
RUN npm install

# GOOD - dependencies cached separately
FROM node:20-alpine
WORKDIR /app

# Copy dependency files first (changes less often)
COPY package.json package-lock.json ./
RUN npm ci --only=production

# Copy source code last (changes most often)
COPY . .
```

### 5. Use `.dockerignore`
```dockerignore
# .dockerignore file
node_modules
npm-debug.log
.git
.gitignore
.env
.env.*
Dockerfile
docker-compose*.yml
*.md
.vscode
.idea
coverage
.nyc_output
dist
```

## Important: Strong Recommendations

### 6. Minimize Layer Count and Size
```dockerfile
# BAD - multiple RUN commands
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN rm -rf /var/lib/apt/lists/*

# GOOD - combined commands, cleanup in same layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        git && \
    rm -rf /var/lib/apt/lists/*
```

### 7. Use COPY Instead of ADD
```dockerfile
# BAD - ADD has magic behavior (auto-extract, fetch URLs)
ADD app.tar.gz /app
ADD https://example.com/file.txt /app/

# GOOD - COPY is explicit and predictable
COPY app/ /app/

# Only use ADD when you need tar extraction
ADD app.tar.gz /app/  # OK - intentionally extracting
```

### 8. Set Explicit WORKDIR
```dockerfile
# BAD - relies on default, uses cd
RUN cd /app && npm install

# GOOD - explicit WORKDIR
WORKDIR /app
RUN npm install
```

### 9. Use ARG for Build-Time Variables
```dockerfile
# GOOD - parameterized builds
ARG NODE_VERSION=20
FROM node:${NODE_VERSION}-alpine

ARG APP_ENV=production
ENV NODE_ENV=${APP_ENV}
```

### 10. Prefer exec Form for CMD and ENTRYPOINT
```dockerfile
# BAD - shell form, doesn't receive signals properly
CMD npm start
ENTRYPOINT /app/start.sh

# GOOD - exec form, proper signal handling
CMD ["npm", "start"]
ENTRYPOINT ["/app/start.sh"]

# GOOD - combining ENTRYPOINT and CMD
ENTRYPOINT ["python"]
CMD ["app.py"]  # Can be overridden
```

## Security

### 11. Don't Store Secrets in Images
```dockerfile
# DANGEROUS - secrets in image layers
ENV API_KEY=secret123
COPY .env /app/
RUN echo "password" > /app/config

# GOOD - use secrets at runtime
# In docker-compose.yml or docker run:
# docker run -e API_KEY=xxx -v ./config:/app/config myimage

# GOOD - use Docker secrets (Swarm) or BuildKit secrets
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci
```

### 12. Scan Images for Vulnerabilities
```dockerfile
# Add to CI pipeline
# docker scout cves myimage:latest
# trivy image myimage:latest
# snyk container test myimage:latest
```

### 13. Use Read-Only Root Filesystem Where Possible
```dockerfile
# In docker-compose.yml
services:
  app:
    image: myapp
    read_only: true
    tmpfs:
      - /tmp
      - /var/run
```

### 14. Drop Capabilities
```dockerfile
# In docker-compose.yml or docker run
services:
  app:
    image: myapp
    cap_drop:
      - ALL
    cap_add:
      - NET_BIND_SERVICE  # Only if needed
```

## Health Checks

### 15. Include HEALTHCHECK
```dockerfile
# GOOD - container health monitoring
FROM node:20-alpine
# ... build steps ...

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

# Or with curl
HEALTHCHECK CMD curl --fail http://localhost:3000/health || exit 1
```

## Metadata

### 16. Add Labels
```dockerfile
# GOOD - image metadata
LABEL org.opencontainers.image.title="My Application"
LABEL org.opencontainers.image.description="Description of the app"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.vendor="My Company"
LABEL org.opencontainers.image.source="https://github.com/org/repo"
```

---

**Quick Reference - Copy This Mental Model:**
- Pin base image versions
- Run as non-root user
- Multi-stage builds
- Order for cache efficiency (deps before code)
- Use `.dockerignore`
- Combine RUN commands, cleanup in same layer
- COPY over ADD
- Explicit WORKDIR
- Exec form for CMD/ENTRYPOINT
- No secrets in images
- Scan for vulnerabilities
- Include HEALTHCHECK
- Add LABEL metadata
