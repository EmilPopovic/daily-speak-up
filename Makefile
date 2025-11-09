setup:
	@bash scripts/setup.sh

install:
	@bash scripts/install.sh

pip:
	.venv/bin/pip install -r backend/requirements.txt

npm:
	cd frontend && npm install && cd ..

dev:
	make backend &
	make email-worker &
	make frontend 

backend:
	.venv/bin/python -m uvicorn backend.src.main:app --host 0.0.0.0 --port 8123

frontend:
	cd frontend && npm run dev

test:
	echo "Test test 1 2 3..."

create-db:
	@echo "Creating database tables..."
	.venv/bin/python -m backend.src.db_manager create

reset-db:
	@echo "Resetting database (this will delete all data)..."
	.venv/bin/python -m backend.src.db_manager reset

reset-db-force:
	@echo "Force resetting database..."
	.venv/bin/python -m backend.src.db_manager reset --force

drop-db:
	@echo "Dropping all database tables..."
	.venv/bin/python -m backend.src.db_manager drop

docker-rabbitmq:
	docker compose -f 'compose.yaml' up -d --build 'rabbitmq'

docker-celery-worker:
	docker compose -f 'compose.yaml' up -d --build 'celery_worker'

email-worker:
	make docker-rabbitmq &
	make docker-celery-worker

.PHONY: setup install pip dev backend frontend test create-db reset-db reset-db-force drop-db
