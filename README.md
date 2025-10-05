# Movie Picture Pipeline

A full-stack application with CI/CD pipelines for displaying movie information. This project includes a Flask backend API and a React frontend application, both deployed on AWS EKS using GitHub Actions.

## Project Structure

```
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
```

## Features

- **Backend API**: Flask application serving movie data
- **Frontend UI**: React application displaying movies
- **CI/CD Pipelines**: Automated testing, building, and deployment
- **Container Orchestration**: Kubernetes deployment on AWS EKS
- **Container Registry**: Docker images stored in Amazon ECR

## Prerequisites

- AWS CLI configured with appropriate permissions
- kubectl configured for EKS cluster
- Docker for local development
- Node.js and npm for frontend development
- Python 3.x for backend development

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hzzxjj/prj4.git
   cd prj4
   ```

2. **Set up AWS credentials in GitHub Secrets:**
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_SESSION_TOKEN`
   - `AWS_REGION` (e.g., us-east-1)

3. **Create EKS cluster:**
   ```bash
   eksctl create cluster --name movie-pipeline --region us-east-1 --nodegroup-name movie-nodes --node-type t3.medium --nodes 2 --nodes-min 1 --nodes-max 3
   ```

4. **Deploy applications:**
   ```bash
   kubectl apply -f deployment/
   ```

5. **Access the applications:**
   - Frontend: Get external IP from `kubectl get svc frontend-service`
   - Backend: Get external IP from `kubectl get svc backend-service`

## API Endpoints

- `GET /api/movies` - Returns list of movies
- `GET /health` - Health check endpoint

## CI/CD Pipelines

### Continuous Integration (CI)
- **Backend CI**: Linting, testing, and building on pull requests
- **Frontend CI**: Linting, testing, and building on pull requests

### Continuous Deployment (CD)
- **Backend CD**: Deploy to EKS on main branch merge
- **Frontend CD**: Deploy to EKS on main branch merge

## Environment Variables

- `REACT_APP_MOVIE_API_URL`: Frontend environment variable for API URL
- `FLASK_ENV`: Backend environment (development/production)

## Monitoring

- Application logs: `kubectl logs -f deployment/backend-deployment`
- Service status: `kubectl get pods,svc,deployments`

## Cleanup

```bash
eksctl delete cluster --name movie-pipeline
aws ecr delete-repository --repository-name movie-backend --force
aws ecr delete-repository --repository-name movie-frontend --force
```
