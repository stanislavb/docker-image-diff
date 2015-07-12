build:
	docker build --force-rm -t $(shell basename $(CURDIR)) .
run:
	docker run -rm -i -v /var/run:/var/run $(shell basename $(CURDIR)) -h
rmi:
	docker rmi $(shell basename $(CURDIR))
