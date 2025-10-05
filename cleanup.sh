# Cleanup script for the Movie Picture Pipeline project

echo "Cleaning up Movie Picture Pipeline resources..."

# Delete Kubernetes resources
echo "Deleting Kubernetes resources..."
kubectl delete -f deployment/ || echo "Some resources may not exist"

# Delete EKS cluster
echo "Deleting EKS cluster..."
eksctl delete cluster --name movie-pipeline --region us-east-1 || echo "Cluster may not exist"

# Delete ECR repositories
echo "Deleting ECR repositories..."
aws ecr delete-repository --repository-name movie-backend --force --region us-east-1 || echo "Backend repository may not exist"
aws ecr delete-repository --repository-name movie-frontend --force --region us-east-1 || echo "Frontend repository may not exist"

echo "Cleanup complete!"
