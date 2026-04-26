.PHONY: requirements install run \
        docker-up docker-up-detached docker-down \
        flake8 mypy black update-requirements

requirements:
	uv export --no-hashes --no-emit-project -o requirements.txt

install:
	uv sync

run:
	docker compose up --build

docker-down:
	docker compose down

flake8:
	uv run flake8 app/

mypy:
	uv run mypy app/

black:
	uv run black app/

update-requirements:  ## Regenerate requirements.txt from pyproject.toml
	uv export --no-hashes --no-emit-project -o requirements.txt
