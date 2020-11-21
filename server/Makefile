.PHONY: help
FLASK_PORT = 5000
APP_NAME = twilio-challenge
FLASK_HOST = 0.0.0.0

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

# DOCKER TASKS
# Build the container
build: ## Build the container
	docker build -t $(APP_NAME) -f Dockerfile .

run: ## Run container on port configured in `config.env`
	docker run -it --rm \
	-p=127.0.0.1:$(FLASK_PORT):$(FLASK_PORT) \
	-e FLASK_HOST=$(FLASK_HOST) \
	-e FLASK_PORT=$(FLASK_PORT) \
	--name="$(APP_NAME)" $(APP_NAME)

stop: ## Stop and remove a running container
	docker stop $(APP_NAME); docker rm $(APP_NAME)

#test:


