# Deployment Guide

## Local Docker Demo

```bash
docker compose up --build
```

Open:

```text
http://localhost:8080/health
```

## Kubernetes Demo

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/ingress.yaml
```

## Terraform Demo

```bash
cd terraform
terraform init
terraform plan
```

Do not apply this in a real cloud account unless reviewed. This is a demo repository.
