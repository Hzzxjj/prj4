# Setup script for the Movie Picture Pipeline project

echo "Setting up Movie Picture Pipeline..."

# Create EKS cluster
echo "Creating EKS cluster..."
eksctl create cluster \
  --name movie-pipeline \
  --region us-east-1 \
  --nodegroup-name movie-nodes \
  --node-type t3.medium \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3 \
  --managed

# Wait for cluster to be ready
echo "Waiting for cluster to be ready..."
kubectl wait --for=condition=Ready nodes --all --timeout=300s

# Create ECR repositories
echo "Creating ECR repositories..."
aws ecr create-repository --repository-name movie-backend --region us-east-1 || echo "Backend repository already exists"
aws ecr create-repository --repository-name movie-frontend --region us-east-1 || echo "Frontend repository already exists"

# Deploy applications
echo "Deploying applications..."
kubectl apply -f deployment/

# Wait for deployments to be ready
echo "Waiting for deployments to be ready..."
kubectl wait --for=condition=Available deployment/backend-deployment --timeout=300s
kubectl wait --for=condition=Available deployment/frontend-deployment --timeout=300s

# Get service URLs
echo "Getting service URLs..."
echo "Backend service:"
kubectl get svc backend-service
echo "Frontend service:"
kubectl get svc frontend-service

echo "Setup complete!"
