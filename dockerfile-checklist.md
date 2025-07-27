# ✅ Dockerfile Best Practices Checklist

Everything you should remember while writing production-grade Dockerfiles.

---

## 🧱 Base and Layers
- [ ] Use minimal and trusted base image (e.g., `alpine`, `debian-slim`)
- [ ] Always pin a specific version (`FROM node:20-alpine`)
- [ ] Combine similar commands into a single `RUN` to minimize image layers

---

## 🧹 Cleanup & Optimization
- [ ] Clean package caches after install (e.g., `rm -rf /var/lib/apt/lists/*`)
- [ ] Use `.dockerignore` to exclude unnecessary files from context
- [ ] Use `COPY` instead of `ADD` unless extracting archives is required

---

## 🔐 Security
- [ ] Never hardcode secrets or tokens in Dockerfile
- [ ] Set a non-root user (`USER appuser`) for running apps
- [ ] Open only the necessary ports with `EXPOSE`

---

## 🚀 Entrypoint & CMD
- [ ] Define behavior via `ENTRYPOINT`
- [ ] Use `CMD` for default arguments to entrypoint
- [ ] Ensure scripts are executable (`chmod +x`) and use shebang (`#!/bin/sh`)

---

## 🧪 Build & Validate
- [ ] Test with `docker build` and `docker run` locally
- [ ] Scan image with `docker scan`, Trivy, or similar
- [ ] Use multi-stage builds for large apps (builder pattern)

---

## 💡 Pro Tips
- [ ] Send logs to stdout/stderr for container logging systems
- [ ] Use `LABEL` for metadata like maintainer info
- [ ] Try to keep the image size small (less attack surface, faster CI/CD)
