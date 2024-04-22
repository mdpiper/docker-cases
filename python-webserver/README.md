# python-webserver

A simple example of setting up, building, and running a Docker image.

The Dockerfile contains instructions for configuring a web server
in Python to display a web page.

Build the image from the Dockerfile with:
```
docker build --tag python-webserver .
```

Launch a container from the image with:
```
docker run --publish 8080:80 --detach --name webby python-webserver
```
Because `--detach` is set, the container runs in the background.
The container is named "webby".
Port 8080 on the local machine is mapped to port 80 in the container.

To view the exciting result of running this container, open 
http://[::]:8080/ (or http://localhost:8080)
in a web browser on your local machine.

Stop the container and remove it with:
```
docker container stop webby
docker container rm webby
```
