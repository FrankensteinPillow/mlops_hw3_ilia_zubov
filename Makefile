predict:
	curl -X POST 127.0.0.1:8000/predict \
	-H "content-type:application/json" \
	-d '{"sepal_length": 1.3, "sepal_width": 2.1, "petal_length": 2.2, "petal_width": 0.8}'

check_health:
	curl 127.0.0.1:8000/health

build:
	docker build -t hw3 .

run:
	uv run fastapi run main.py

run_docker:
	docker rm -f hw3 && docker run --name hw3 -p 8000:8000 hw3

compose:
	docker compose -f docker-compose.blue.yaml -f docker-compose.green.yaml -f docker-compose.nginx.yaml up

format:
	ruff check --select I,F401 --fix . && ruff format --line-length 79 .
