# Git Generation Checklist

**Read this BEFORE writing Git commands. Safety and clarity matter.**

## Critical: You Must Do These

### 1. Never Force Push to Shared Branches
```bash
# DANGEROUS - rewrites history others depend on
git push --force origin main
git push -f origin develop

# SAFER - force-with-lease checks for remote changes
git push --force-with-lease origin feature-branch

# SAFEST - only force push to YOUR branches
git push --force origin my-feature-branch  # OK if only you use it
```

### 2. Always Review Before Commit
```bash
# Check what you're about to commit
git status
git diff --staged

# Review unstaged changes too
git diff

# Don't blindly add everything
git add -A  # Careful! Adds ALL files

# BETTER - add specific files
git add src/feature.js tests/feature.test.js

# BEST - review each change interactively
git add -p  # Patch mode: review each hunk
```

### 3. Write Meaningful Commit Messages
```bash
# BAD - unclear, unhelpful
git commit -m "fix"
git commit -m "updates"
git commit -m "WIP"

# GOOD - follows conventional format
git commit -m "fix: resolve null pointer in user authentication"
git commit -m "feat: add export to CSV functionality"
git commit -m "docs: update API documentation for v2 endpoints"

# Format: <type>: <description>
# Types: feat, fix, docs, style, refactor, test, chore
```

### 4. Never Commit Secrets
```bash
# Check for secrets before commit
git diff --staged | grep -i "password\|secret\|api.key\|token"

# Use .gitignore for sensitive files
echo ".env" >> .gitignore
echo "*.pem" >> .gitignore
echo "credentials.json" >> .gitignore

# If you accidentally committed secrets:
# 1. Rotate the secret IMMEDIATELY
# 2. Remove from history (see git filter-branch or BFG)
# 3. Force push (coordinate with team)
```

### 5. Pull Before Push
```bash
# GOOD - incorporate remote changes first
git pull --rebase origin main
git push origin main

# Or use fetch + rebase for more control
git fetch origin
git rebase origin/main
git push
```

## Important: Strong Recommendations

### 6. Use Branches for All Work
```bash
# BAD - working directly on main
git checkout main
# edit files...
git commit

# GOOD - feature branch workflow
git checkout -b feature/user-authentication
# edit files...
git commit
git push -u origin feature/user-authentication
# Create PR/MR
```

### 7. Keep Commits Atomic
```bash
# BAD - one commit with unrelated changes
git add .
git commit -m "fix bug, add feature, update docs, refactor"

# GOOD - separate commits for each change
git add src/auth.js
git commit -m "fix: handle expired tokens in auth module"

git add src/export.js
git commit -m "feat: add PDF export option"

git add README.md
git commit -m "docs: document PDF export feature"
```

### 8. Use Interactive Rebase to Clean History
```bash
# Clean up before merging to main
git rebase -i HEAD~5  # Last 5 commits

# In editor:
# pick abc123 First commit
# squash def456 WIP
# squash ghi789 More WIP
# reword jkl012 Final feature

# Result: cleaner history
```

### 9. Stash Work in Progress
```bash
# Save work without committing
git stash push -m "WIP: user profile feature"

# List stashes
git stash list

# Apply and keep in stash
git stash apply stash@{0}

# Apply and remove from stash
git stash pop

# Apply specific stash
git stash apply stash@{2}
```

### 10. Use Git Aliases for Common Commands
```bash
# Add to ~/.gitconfig
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    unstage = reset HEAD --
    last = log -1 HEAD
    graph = log --oneline --graph --decorate --all
    amend = commit --amend --no-edit
```

## Safety Commands

### 11. Know How to Undo
```bash
# Undo last commit (keep changes staged)
git reset --soft HEAD~1

# Undo last commit (keep changes unstaged)
git reset HEAD~1

# Undo last commit (discard changes) - DESTRUCTIVE
git reset --hard HEAD~1

# Undo a specific file change
git checkout -- path/to/file

# Revert a pushed commit (creates new commit)
git revert <commit-hash>

# Find lost commits
git reflog
git checkout <lost-commit-hash>
```

### 12. Use `--dry-run` for Destructive Operations
```bash
# See what would be deleted
git clean -n -d
git clean --dry-run -d

# See what would be pushed
git push --dry-run origin main

# See what rebase would do
git rebase --interactive --exec "echo" origin/main
```

### 13. Protect Important Branches
```bash
# Configure locally (won't push to protected branch)
git config --local receive.denyCurrentBranch refuse

# Better: Configure branch protection in GitHub/GitLab
# - Require pull request reviews
# - Require status checks
# - Disable force push
```

## Merge Strategies

### 14. Choose the Right Merge Strategy
```bash
# Regular merge (creates merge commit)
git merge feature-branch

# Squash merge (single commit, no merge commit)
git merge --squash feature-branch
git commit -m "feat: add user authentication"

# Rebase (linear history)
git rebase main
git checkout main
git merge feature-branch  # Fast-forward

# When to use which:
# - merge: preserving full history matters
# - squash: want clean history, feature is many small commits
# - rebase: want linear history, comfortable with rebasing
```

### 15. Handle Merge Conflicts Properly
```bash
# When conflict occurs:
git status  # See conflicted files

# Edit files to resolve (look for <<<<<<< markers)
# Then:
git add resolved-file.js
git commit  # Or git rebase --continue

# Abort if needed
git merge --abort
git rebase --abort

# Use merge tool
git mergetool
```

## Collaboration

### 16. Keep Your Fork Updated
```bash
# Add upstream remote
git remote add upstream https://github.com/original/repo.git

# Fetch and merge upstream changes
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# Or rebase your feature branch
git checkout feature-branch
git rebase upstream/main
```

---

**Quick Reference - Copy This Mental Model:**
- Never force push shared branches
- Review changes before commit (`git diff --staged`)
- Meaningful commit messages (type: description)
- Never commit secrets (use .gitignore)
- Pull/rebase before push
- Feature branches for all work
- Atomic commits (one change per commit)
- Interactive rebase to clean history
- Know your undos (reset, revert, reflog)
- `--dry-run` for destructive commands
- Right merge strategy for the situation
- Keep fork updated with upstream
