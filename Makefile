.PHONY: all run tests lint

WORDDIR=.
BLACKFLAGS=--target-version=py312

all: run tests lint

run:
	@echo "Starting server..."
	@poetry run uvicorn main:app --host 0.0.0.0 --port 8000

tests:
	@echo "Running tests..."
	@poetry run pytest $(WORDDIR)/tests

lint:
	@echo "Linting..."
	@poetry run black $(WORDDIR) $(BLACKFLAGS)
	@echo "Linting done"
