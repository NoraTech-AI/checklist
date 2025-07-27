# ✅ Kubernetes Manifest YAML Checklist

Key points to write safe, maintainable, and scalable Kubernetes YAML files.

---

## 📄 Basics
- [ ] Always specify correct `apiVersion` and `kind`
- [ ] Add meaningful `metadata.name` and use consistent `labels`
- [ ] Separate resources into multiple YAMLs (`deployment.yaml`, `service.yaml`, etc.)

---

## 📦 Deployments
- [ ] Add `readinessProbe` and `livenessProbe`
- [ ] Set resource `requests` and `limits` properly
- [ ] Use `rollingUpdate` strategy to minimize downtime

---

## 🔐 Config & Security
- [ ] Use `ConfigMap` for application settings
- [ ] Use `Secret` for sensitive data like passwords, tokens, and keys
- [ ] Set `securityContext` and `runAsNonRoot: true` where applicable

---

## 📡 Networking
- [ ] Expose only required ports
- [ ] Use `ClusterIP` for internal communication
- [ ] Use `Ingress` or `LoadBalancer` only when necessary

---

## 🧪 Testing & Validation
- [ ] Run `kubectl apply --dry-run=client -f` before deploying
- [ ] Use `kubectl explain` to understand YAML fields
- [ ] Use `kubectl logs`, `describe`, and `get` to debug issues

---

## 💡 Pro Tips
- [ ] Standardize labels (`app`, `env`, `tier`, etc.)
- [ ] Use `kubeval`, `kube-score`, or `datree` for schema validation
- [ ] Document each YAML (comment on purpose and parameters)
