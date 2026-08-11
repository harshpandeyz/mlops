# MLOps Lifecycle – Sample Machine Learning Project

## Assignment: Git Repository Setup and MLOps Lifecycle Documentation

This repository demonstrates a basic **MLOps workflow** for a sample Machine Learning project. It covers Git-based version control, branching strategy, data and model management, experiment tracking, model training, validation, deployment, monitoring, and retraining.

---

## 1. Objective

The objectives of this assignment are:

- Set up a Git repository for an ML project.
- Implement a proper Git branching strategy.
- Maintain separate `main`, `dev`, and `feature/*` branches.
- Document the complete MLOps lifecycle.
- Demonstrate reproducibility and version control.
- Understand how ML development moves from experimentation to production.
- Establish a foundation for CI/CD and automated ML workflows.

---

# 2. MLOps Lifecycle

The project follows the following lifecycle:

```text
Data Collection
      ↓
Data Validation
      ↓
Data Versioning
      ↓
Data Preprocessing
      ↓
Model Training
      ↓
Experiment Tracking
      ↓
Model Validation
      ↓
Model Versioning
      ↓
Model Packaging
      ↓
Deployment
      ↓
Monitoring
      ↓
Drift Detection
      ↓
Retraining
      ↓
Redeployment

## Git Branching Strategy
Development follows main, dev, and feature/* branches.
