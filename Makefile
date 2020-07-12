# Docker-Compose commands
stack_up:
	docker-compose up --build -d

stack_up_skip_cache:
	docker-compose build --no-cache
	docker-compose up -d

stack_down:
	docker-compose down

stack_logs:
	docker-compose logs -f