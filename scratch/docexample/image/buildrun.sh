docker stop helloteam
docker rm helloteam
docker build -t helloteam .
docker run --name helloteam  -h helloteam -d  -p 5000:5000 helloteam
