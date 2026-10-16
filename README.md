# Project 03: Automated CI/CD Pipeline with GitHub Actions

## 📌 Project Overview
This project demonstrates how to set up an automated **Continuous Integration and Continuous Deployment (CI/CD)** pipeline using **GitHub Actions** for a **Python** application. The main objective is to automate code testing and linting on every `push` or `pull_request` to ensure high code quality and prevent broken code from reaching production.

---

## 🏗 CI/CD Workflow & Architecture
```text
Developer Push Code → [ GitHub Repository ] → [ Trigger GitHub Actions Workflow ]
                                                     │
                                                     ├── 1. Set up Python Environment
                                                     ├── 2. Install Dependencies
                                                     └── 3. Run Automated Tests (test_app.py)