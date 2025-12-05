FROM python:3.12-slim

ENV MODEL_PATH=model.pkl
ENV MODEL_VERSION=v1.0.0

WORKDIR /app

COPY . .

RUN apt update && \
    apt install curl -y && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

RUN /root/.local/bin/uv self update && \
    /root/.local/bin/uv sync --no-cache

EXPOSE 8000

CMD ["/root/.local/bin/uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]
