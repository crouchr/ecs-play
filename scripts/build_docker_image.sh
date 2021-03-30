cd ..
docker build -t test-service .
docker tag test-service registry:5000/test-service:latest
docker push registry:5000/test-service:latest
docker rmi test-service:latest
