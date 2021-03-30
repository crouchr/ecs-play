# Use a compose file started from rc.local
docker run --name test-service \
-p 8081:8081 \
-d \
test-service
