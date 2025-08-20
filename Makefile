.PHONY: help install test lint format clean dashboard

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install Python dependencies
	pip install -r requirements.txt

install-dev:  ## Install development dependencies
	pip install -r requirements.txt
	pip install pytest pytest-cov black flake8

test:  ## Run unit tests
	pytest tests/ -v

test-cov:  ## Run tests with coverage
	pytest tests/ --cov=src --cov-report=html --cov-report=term

lint:  ## Run linting checks
	flake8 src/ tests/ --max-line-length=88 --ignore=E203,W503

format:  ## Format code with black
	black src/ tests/

clean:  ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -f .coverage

dashboard:  ## Start the analytical dashboard
	@echo "Starting backend..."
	@cd scripts/backend && python app.py &
	@echo "Starting frontend..."
	@cd scripts/frontend && npm start

dashboard-backend:  ## Start only the backend API
	@cd scripts/backend && python app.py

dashboard-frontend:  ## Start only the frontend
	@cd scripts/frontend && npm start

install-frontend:  ## Install frontend dependencies
	@cd scripts/frontend && npm install

build-frontend:  ## Build frontend for production
	@cd scripts/frontend && npm run build
