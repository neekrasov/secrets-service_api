run-local:
	@echo "Running locally..."
	python3.11 main.py

run:
	docker-compose up

build:
	docker-compose build
