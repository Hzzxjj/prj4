Movie Picture Pipeline, a full-stack project I built with a Flask backend and React frontend, both containerized with Docker and deployed on AWS EKS using GitHub Actions CI/CD. It includes automated testing, ECR image builds, and Kubernetes deployment with LoadBalancer services. The app displays movie info through a clean, responsive UI. Everything from setup to deployment is fully automated and production-ready.

Project Structure
├── backend/                 # Flask API application
│   ├── app.py              # Main Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Backend container configuration
│   └── test_app.py         # Backend tests
├── frontend/               # React application
│   ├── src/                # React source code
│   ├── package.json        # Node.js dependencies
│   ├── Dockerfile          # Frontend container configuration
│   └── public/             # Static assets
├── deployment/             # Kubernetes manifests
│   ├── backend-deployment.yaml
│   ├── frontend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-service.yaml
│   └── configmap.yaml
└── .github/workflows/      # GitHub Actions CI/CD pipelines
    ├── backend-ci.yaml     # Backend CI pipeline
    ├── frontend-ci.yaml    # Frontend CI pipeline
    ├── backend-cd.yaml     # Backend CD pipeline
    └── frontend-cd.yaml    # Frontend CD pipeline
