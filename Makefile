up:  # Start container
	docker-compose -f docker-compose.yml up

down:  # Stop running container
	docker-compose -f docker-compose.yml down

build:  # Build container
	docker-compose -f docker-compose.yml build

test:  # Run tests
	pytest -vv
