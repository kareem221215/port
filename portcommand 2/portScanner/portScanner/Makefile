install:
	@echo "Installing..."
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	@echo "Installed"

format:
	@echo "Formatting..."
	black *.py */*.py
	@echo "Formatted"

lint:
	@echo "Linting..."
	pylint --disable=R,C,E1121 *.py */*.py
	@echo "Linted"

test:
	@echo "Testing..."
	pytest -v *.py
	@echo "Tested"

all: install format lint test