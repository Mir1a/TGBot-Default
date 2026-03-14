.PHONY: requirements install run \
        docker-up docker-up-detached docker-down \
        flake8 mypy black

requirements:
	uv export --no-hashes --no-emit-project -o requirements.txt

install:
	uv sync

run:
	uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

docker-up:
	docker compose up --build

docker-up-detached:
	docker compose up -d --build

docker-down:
	docker compose down

flake8:
	uv run flake8 app/

mypy:
	uv run mypy app/

black:
	uv run black app/
