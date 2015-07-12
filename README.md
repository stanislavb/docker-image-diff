Docker image hash
=================

Retrieve image hash from local cache and from remote registry.

Build it yourself
-----------------
```
make build
```

Run it from Docker Hub
----------------------
```
docker run --rm -i -v /var/run:/var/run stanislavb/docker-image-hash python:3-onbuild
```
