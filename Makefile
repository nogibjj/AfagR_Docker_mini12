# # Variables
# APP_NAME := workout_app
# DOCKER_USERNAME :=  afagramazanova # Replace with your Docker Hub username
# IMAGE_NAME := $(DOCKER_USERNAME)/$(APP_NAME):workout_app
# CONTAINER_PORT := 5000
# HOST_PORT := 5000

# .PHONY: all build run stop test push clean

# # Build the Docker image
# build:
# 	docker build -t $(APP_NAME) .

# # Run the Docker container
# run:
# 	docker run -d -p $(HOST_PORT):$(CONTAINER_PORT) --name $(APP_NAME) $(APP_NAME)

# # Stop and remove the Docker container
# stop:
# 	docker stop $(APP_NAME) || true
# 	docker rm $(APP_NAME) || true

# install:
# 	pip install -r requirements.txt

# # Push the Docker image to Docker Hub
# push:
# 	docker tag $(APP_NAME) $(IMAGE_NAME)
# 	docker push $(IMAGE_NAME)

# # Test the application
# test:
# 	python -m pytest

# # Clean up Docker resources
# clean: stop
# 	docker rmi $(APP_NAME) || true
# 	docker rmi $(IMAGE_NAME) || true

# # Build, run, and test in one step
# all: build run test

# Variables
APP_NAME := workout_app
DOCKER_USERNAME := afagramazanova
IMAGE_NAME := $(DOCKER_USERNAME)/$(APP_NAME):latest
CONTAINER_PORT := 5000
HOST_PORT := 5000

.PHONY: all build run stop install test push clean

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
	docker run -d -p $(HOST_PORT):$(CONTAINER_PORT) --name $(APP_NAME) $(IMAGE_NAME)

# Stop and remove the Docker container
stop:
	docker stop $(APP_NAME) || true
	docker rm $(APP_NAME) || true

# Install dependencies
install:
	pip install -r requirements.txt

# Push the Docker image to Docker Hub
push:
	docker push $(IMAGE_NAME)

# Test the application
test:
	python -m pytest tests/test_app.py

# Clean up Docker resources
clean: stop
	docker rmi $(IMAGE_NAME) || true

# Build, run, and test in one step
all: build run test