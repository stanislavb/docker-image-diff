Docker image diff
=================

Check if your locally cached image is the same as on Docker Hub. Takes image and optional tag as input. If tag is omitted, 'latest' is assumed.

Return codes:
* 0 if images are the same
* 1 on error (like registry being offline)
* 2 if images differ or image not locally cached
* 3 if image not found in registry

Limitations
-----------
* Errors out on SSL verification when using boot2docker.
* Untested with private registry.

Build it yourself
-----------------
```
make build
```

Run it from Docker Hub
----------------------
```
docker run --rm -i -v /var/run/docker.sock:/var/run/docker.sock stanislavb/docker-image-diff python:3-onbuild
```
