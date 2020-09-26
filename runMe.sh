docker build -t (your-repo-name):latest ./app_package
docker push (your-repo-name):latest
kubectl apply -f ./k8s/deployment.yaml
