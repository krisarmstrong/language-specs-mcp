# Versioning

This project follows Semantic Versioning (SemVer): https://semver.org/

## Versioning Rules

- MAJOR: incompatible API changes
- MINOR: backwards-compatible feature additions
- PATCH: backwards-compatible bug fixes

## Release Checklist

1. Update `CHANGELOG.md`
2. Bump `package.json` version
3. Run `npm run lint` and `npm run build`
4. Tag the release: `git tag vX.Y.Z`
5. Push tags: `git push --tags`
