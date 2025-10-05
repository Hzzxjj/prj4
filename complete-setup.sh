#!/bin/bash

# Movie Picture Pipeline - Complete Setup Script
# Run this script with fresh AWS credentials

echo "🎬 MOVIE PICTURE PIPELINE - COMPLETE SETUP"
echo "=========================================="

# Check if AWS CLI is configured
if ! aws sts get-caller-identity > /dev/null 2>&1; then
    echo "❌ AWS CLI not configured or credentials expired"
    echo "Please configure AWS CLI with: aws configure"
    exit 1
fi

echo "✅ AWS CLI configured"

# Set variables
REGION="us-east-1"
CLUSTER_NAME="movie-pipeline"
BACKEND_REPO="movie-backend"
FRONTEND_REPO="movie-frontend"

echo "🚀 Creating EKS cluster: $CLUSTER_NAME"
eksctl create cluster \
    --name $CLUSTER_NAME \
    --region $REGION \
    --nodegroup-name movie-nodes \
    --node-type t3.medium \
    --nodes 2 \
    --nodes-min 1 \
    --nodes-max 3 \
    --managed \
    --with-oidc \
    --ssh-access \
    --ssh-public-key ~/.ssh/id_rsa.pub

if [ $? -eq 0 ]; then
    echo "✅ EKS cluster created successfully"
else
    echo "❌ Failed to create EKS cluster"
    exit 1
fi

echo "🐳 Creating ECR repositories"
aws ecr create-repository --repository-name $BACKEND_REPO --region $REGION || echo "Backend repo already exists"
aws ecr create-repository --repository-name $FRONTEND_REPO --region $REGION || echo "Frontend repo already exists"

echo "✅ ECR repositories created"

echo "☸️ Configuring kubectl"
aws eks update-kubeconfig --region $REGION --name $CLUSTER_NAME

echo "📦 Deploying applications to Kubernetes"
kubectl apply -f deployment/

echo "⏳ Waiting for deployments to be ready"
kubectl wait --for=condition=Available deployment/backend-deployment --timeout=300s
kubectl wait --for=condition=Available deployment/frontend-deployment --timeout=300s

echo "🌐 Getting service URLs"
echo "Backend service:"
kubectl get svc backend-service
echo ""
echo "Frontend service:"
kubectl get svc frontend-service

echo ""
echo "🎉 SETUP COMPLETE!"
echo "=================="
echo "Your Movie Picture Pipeline is now running on AWS EKS!"
echo ""
echo "Next steps:"
echo "1. Get the external IPs from the services above"
echo "2. Test the backend API: curl http://<BACKEND_IP>:5000/api/movies"
echo "3. Open the frontend: http://<FRONTEND_IP>"
echo "4. Create a pull request to test CI pipelines"
echo "5. Merge to main to test CD pipelines"
echo ""
echo "To clean up resources later, run: ./cleanup.sh"
