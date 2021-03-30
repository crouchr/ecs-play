cd ..
docker build -t test-service .
docker tag test-service registry:5000/test-service:$VERSION

# push to local registry
docker push registry:5000/test-service:$VERSION

# push to DockerHub so that it can be pulled into AWS ECS
docker push test-service:$VERSION

# clean up
docker rmi test-service
