cd ..
docker build -t test-service .
docker tag test-service registry:5000/test-service:$VERSION
docker push registry:5000/test-service:$VERSION
docker rmi test-service
