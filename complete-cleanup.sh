#!/bin/bash

# Movie Picture Pipeline - Cleanup Script

echo "🧹 CLEANING UP MOVIE PICTURE PIPELINE RESOURCES"
echo "=============================================="

REGION="us-east-1"
CLUSTER_NAME="movie-pipeline"
BACKEND_REPO="movie-backend"
FRONTEND_REPO="movie-frontend"

echo "☸️ Deleting Kubernetes resources"
kubectl delete -f deployment/ 2>/dev/null || echo "Some resources may not exist"

echo "🗑️ Deleting EKS cluster: $CLUSTER_NAME"
eksctl delete cluster --name $CLUSTER_NAME --region $REGION || echo "Cluster may not exist"

echo "🐳 Deleting ECR repositories"
aws ecr delete-repository --repository-name $BACKEND_REPO --force --region $REGION 2>/dev/null || echo "Backend repository may not exist"
aws ecr delete-repository --repository-name $FRONTEND_REPO --force --region $REGION 2>/dev/null || echo "Frontend repository may not exist"

echo "✅ CLEANUP COMPLETE!"
echo "All resources have been removed."
