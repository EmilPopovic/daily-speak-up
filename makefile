setup:
	@bash scripts/setup.sh

install:
	@bash scripts/install.sh

dev:
	make backend &
	make frontend

backend:
	echo "hello"

frontend:
	cd frontend && npm run dev

test:
	echo "Test test 1 2 3..."

.PHONY: setup install dev backend frontend test
