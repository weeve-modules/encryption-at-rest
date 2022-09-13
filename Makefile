SHELL := /bin/bash # to enable source command in run_app

MODULE=weevenetwork/encryption-at-rest
VERSION_NAME=v1.0.0

install_dev:
	python3 -m pip install -r requirements_dev.txt
.PHONY: install_dev

lint:
	black src/ test/
	flake8 src/ test/
.PHONY: lint

run_app:
	set -a && source .env && set +a && python src/main.py
.PHONY: run_app

create_image:
	docker build -t ${MODULE}:${VERSION_NAME} . -f docker/Dockerfile
.PHONY: create_image

run_image:
	docker run -p 80:80 --rm --env-file=./.env ${MODULE}:${VERSION_NAME}
.PHONY: run_image

debug_image:
	docker run -p 80:80 --rm --env-file=./.env --entrypoint /bin/bash -it ${MODULE}:${VERSION_NAME}
.PHONY: debug_image

run_docker_compose:
	docker-compose -f docker/docker-compose.yml up
.PHONY: run_docker_compose

stop_docker_compose:
	docker-compose -f docker/docker-compose.yml down
.PHONY: stop_docker_compose

run_test:
	# For more verbose output you can add [-s] option
	pytest test/boilerplate_test.py -v
.PHONY: run_test

push_latest:
	docker image push ${MODULE}:${VERSION_NAME}
.PHONY: push_latest

create_and_push_multi_platform:
	docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v6,linux/arm/v7 -t ${MODULE}:${VERSION_NAME} --push . -f docker/Dockerfile
.PHONY: create_and_push_multi_platform

run_listener:
	docker run --rm -p 8000:8000 \
	-e PORT=8000 \
	-e LOG_HTTP_BODY=true \
	-e LOG_HTTP_HEADERS=true \
	--name listener \
	jmalloc/echo-server
.PHONY: run_listener
