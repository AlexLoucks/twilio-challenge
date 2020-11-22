.PHONY: help
FLASK_PORT = 5000
APP_NAME = twilio-challenge
FLASK_HOST = 0.0.0.0
FLASK_ENV = dev

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

# DOCKER TASKS
# Build the container
build: ## Build the container
	docker build -t $(APP_NAME) --target runnable -f Dockerfile .

run: ## Run container on port 5000
	docker run -it --rm \
	-p $(FLASK_PORT):$(FLASK_PORT) \
	-e FLASK_HOST=$(FLASK_HOST) \
	-e FLASK_PORT=$(FLASK_PORT) \
	-e FLASK_ENV=$(FLASK_ENV) \
	--name="$(APP_NAME)" $(APP_NAME)

run-detached: ## Run container on port 5000, in detached mode
	docker run -it --rm -d\
	-p $(FLASK_PORT):$(FLASK_PORT) \
	-e FLASK_HOST=$(FLASK_HOST) \
	-e FLASK_PORT=$(FLASK_PORT) \
	-e FLASK_ENV=$(FLASK_ENV) \
	--name="$(APP_NAME)" $(APP_NAME)

stop: ## Stop and remove a running container
	docker stop $(APP_NAME); docker rm $(APP_NAME)

build-test: ## Build  a test container 
	docker build -t $(APP_NAME)-test --target tests -f Dockerfile .

run-test: ## Run unit tests in test container
	docker run -it --rm \
	-p $(FLASK_PORT):$(FLASK_PORT) \
	-e FLASK_HOST=$(FLASK_HOST) \
	-e FLASK_PORT=$(FLASK_PORT) \
	-e FLASK_ENV=$(FLASK_ENV) \
	--name="$(APP_NAME)-test" $(APP_NAME)-test


