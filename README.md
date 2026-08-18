# Secure Software Supply Chain

A security-focused DevSecOps project that demonstrates how to build, scan, verify, sign, attest, and securely deploy a containerized application using a modern software supply-chain security pipeline.

The project integrates automated security checks into GitHub Actions and deploys an immutable, cryptographically signed container image to Kubernetes using Helm.

---

## Project Overview

Modern software supply chains can be compromised through vulnerable dependencies, leaked secrets, insecure source code, compromised container images, or tampered artifacts.

This project implements a secure CI/CD workflow that provides multiple layers of protection:

- Static Application Security Testing (SAST)
- Secret detection
- Dependency vulnerability scanning
- Container vulnerability scanning
- Software Bill of Materials (SBOM)
- SLSA build provenance
- Container image signing with Cosign
- Cryptographic image verification
- Immutable digest-based Kubernetes deployment
- Kubernetes security hardening
- Helm-based deployment

The goal is to ensure that an application is not only built successfully, but that its software artifacts can also be **scanned, traced, verified, and securely deployed**.

---

#  Architecture

```text
                    ┌──────────────────────┐
                    │   Developer / Git    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    GitHub Actions    │
                    │      Secure CI       │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
         ┌─────────┐      ┌──────────┐    ┌──────────┐
         │ Semgrep │      │ Gitleaks │    │pip-audit │
         │  SAST   │      │  Secrets │    │  Deps    │
         └─────────┘      └──────────┘    └──────────┘
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │   Docker Image Build │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
          ┌────────────┐              ┌────────────┐
          │   Trivy    │              │    Syft    │
          │ Container  │              │    SBOM    │
          │   Scan     │              │ Generation │
          └────────────┘              └────────────┘
                 │                           │
                 └─────────────┬─────────────┘
                               ▼
                    ┌──────────────────────┐
                    │   Docker Registry    │
                    │     Image Publish    │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
        ┌────────────────┐          ┌────────────────┐
        │ SLSA Provenance│          │     Cosign     │
        │    Attestation │          │ Image Signing  │
        └────────────────┘          └────────────────┘
                 │                           │
                 └─────────────┬─────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Immutable Image      │
                    │ SHA256 Digest        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │        Helm          │
                    │      Deployment      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Kubernetes      │
                    │       Minikube       │
                    └──────────────────────┘