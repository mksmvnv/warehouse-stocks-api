.PHONY: all run lint

WORDDIR=./
BLACKFLAGS=--target-version=py312

all: run lint

run:
	@echo "Starting server..."
	@poetry run uvicorn main:app --host 0.0.0.0 --port 8000

lint:
	@echo "Linting..."
	@poetry run black $(WORDDIR) $(BLACKFLAGS)
	@echo "Linting done"
