FROM python:3.13-slim

WORKDIR /app

# Install curl for health check and nc for checking postgres
RUN apt-get update && apt-get install -y \
    curl \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8123

# Wait for Postgres and create missing tables
ENTRYPOINT ["sh", "-c", "\
    echo 'Waiting for Postgres...'; \
    while ! nc -z postgres 5432; do sleep 1; done; \
    echo 'Postgres is up! Running db_manager create...'; \
    python -m src.db_manager create; \
    echo 'Starting backend...'; \
    exec python -m uvicorn src.main:app --host 0.0.0.0 --port 8123 \
"]
