**Docker Commands:**
- Login to Docker Hub
docker login

- Build Docker images
docker build -t mennidiskind/contacts-api:v1 ./app

- Push images to registry
docker push mennidiskind/contacts-api:v1


**Kubernetes Commands:**
- Apply/create resources from YAML files
kubectl apply -f k8s/

- Get/list resources (pods, services)
kubectl get pods
kubectl get services

- View pod logs
kubectl logs api
kubectl logs mongodb

- Describe resources for debugging
kubectl describe pod api
kubectl describe pod mongodb
kubectl describe service api-service

- Delete resources
kubectl delete -f k8s/


**Minikube Commands:**
- Start/stop cluster
minikube start
minikube stop

- Get service URLs
minikube service api-service --url

- Get cluster IP address
minikube ip


**Testing Commands:**
- Make HTTP requests to test API endpoints (GET, POST, PUT, DELETE)

* GET = url/contacts

* POST = url/contacts -H "Content-Type: application/json" \
-d '{"first_name":"John","last_name":"Doe","phone_number":"050-1234567"}'

* PUT = url/contacts/<ID> -H "Content-Type: application/json" \
-d '{"first_name":"Menni","last_name":"Diskind","phone_number":"050-1231231"}'

* DELETE url/contacts/<ID>
