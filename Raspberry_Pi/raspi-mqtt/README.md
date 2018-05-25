# rpi-mosquitto

Raspberry Pi compatible Docker Image with mosquitto MQTT broker.
Based upon [docker-mosquitto](https://github.com/toke/docker-mosquitto).

## How to run

```
docker run -tip 1883:1883 -p 9001:9001 pascaldevink/rpi-mosquitto
```

Exposes Port 1883 (MQTT) 9001 (Websocket MQTT)

Alternatively you can use volumes to make the changes persistent and change the configuration.
```
mkdir -p /srv/mqtt/config/
mkdir -p /srv/mqtt/data/
mkdir -p /srv/mqtt/log/
# place your mosquitto.conf in /srv/mqtt/config/
# NOTE: You have to change the permissions of the directories
# to allow the user to read/write to data and log and read from
# config directory
# For TESTING purposes you can use chmod -R 777 /srv/mqtt/*
# Better use "-u" with a valid user id on your docker host

docker run -ti -p 1883:1883 -p 9001:9001 \
-v /srv/mqtt/config:/mqtt/config:ro \
-v /srv/mqtt/log:/mqtt/log \
-v /srv/mqtt/data/:/mqtt/data/ \
--name mqtt pascaldevink/rpi-mosquitto
```

## How to create this image

Run all the commands from within the project root directory.

### Build the Docker Image
```bash
make build
```

#### Push the Docker Image to the Docker Hub
* First use a `docker login` with username, password and email address
* Second push the Docker Image to the official Docker Hub

```bash
make push
```

## License

The MIT License (MIT)
