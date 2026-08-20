#  Secure Software Supply Chain

A production-oriented **DevSecOps and software supply-chain security platform** that secures the software lifecycle from source code to container deployment.

The project implements automated security scanning, dependency analysis, secret detection, container vulnerability scanning, SBOM generation, artifact signing, SLSA build provenance, and Kubernetes admission control using Kyverno.

---

##  Project Overview

Modern applications depend on numerous components:

- Source code
- Third-party dependencies
- Container images
- CI/CD pipelines
- Build systems
- Kubernetes deployments

A compromise at any stage of the software supply chain can introduce malicious or vulnerable components into production.

This project addresses that problem by implementing security controls across the complete software delivery lifecycle.

### Security Pipeline

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── SAST
    │    └── Semgrep
    │
    ├── Secret Scanning
    │    └── Gitleaks
    │
    ├── Dependency Scanning
    │    └── pip-audit
    │
    ├── Container Security
    │    └── Trivy
    │
    ├── SBOM Generation
    │    └── Syft
    │
    ├── Image Publishing
    │    └── Docker Hub
    │
    ├── Build Provenance
    │    └── SLSA
    │
    └── Image Signing
         └── Cosign
              │
              ▼
        Docker Registry
              │
              ▼
          Kubernetes
              │
              ▼
           Kyverno
              │
       ┌──────┴─────────┐
       │                │
       ▼                ▼
 Image Verification   Pod Security
       │                │
       │          ├── Non-root
       │          ├── No privilege escalation
       │          ├── No privileged containers
       │          └── Read-only filesystem
       │
       ▼
    Deployment