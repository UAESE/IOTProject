docker stop apiserverC
docker rm apiserverC
docker build -t apiserver .
docker run --name apiserverC  -d  -p 5001:5001 apiserver
