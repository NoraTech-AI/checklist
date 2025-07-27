# ✅ Docker Compose File Checklist

A practical checklist to write reliable, secure, and production-friendly `docker-compose.yml` files.

---

## 🧱 Basic Structure
- [ ] Use version key at the top (`version: "3.8"` or appropriate)
- [ ] Define services under the `services:` block
- [ ] Use consistent and meaningful service names

---

## 🧩 Networking & Volumes
- [ ] Define custom networks when needed for isolation
- [ ] Use named volumes for data persistence (`volumes:` block)
- [ ] Avoid hardcoding paths inside containers

---

## 🛠 Service Configuration
- [ ] Always specify `image:` or `build:` for services
- [ ] Use `depends_on` to manage startup order
- [ ] Set environment variables via `.env` file or `environment:` block
- [ ] Mount configuration files cleanly via `volumes:` (e.g. configs, certs)

---

## 🔐 Security & Reliability
- [ ] Avoid using `privileged: true` unless absolutely necessary
- [ ] Use `restart: unless-stopped` or `always` for long-running services
- [ ] Avoid storing secrets in plaintext `.yml` files

---

## 🧪 Testing & Dev
- [ ] Use `profiles:` if you want to toggle services in dev/test/prod
- [ ] Confirm with `docker-compose config` for YAML correctness
- [ ] Test with `docker-compose up` and `logs` for initial debugging

---

## 💡 Pro Tips
- [ ] Use `.dockerignore` to reduce build context
- [ ] Separate local dev and production Compose files (`docker-compose.override.yml`)
- [ ] Use `healthcheck:` blocks for service readiness
