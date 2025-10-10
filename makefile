setup:
	@bash scripts/setup.sh

install:
	@bash scripts/install.sh

dev:
	make backend &
	make frontend

backend:
	.venv/bin/python -m uvicorn backend.src.main:app --host 0.0.0.0 --port 8123

frontend:
	cd frontend && npm run dev

test:
	echo "Test test 1 2 3..."

.PHONY: setup install dev backend frontend test
