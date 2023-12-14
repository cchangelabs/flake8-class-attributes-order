PYTHON=3.11.6

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=flake8_class_attributes_order --cov-report=xml

types:
	poetry run mypy .

flake8:
	poetry run flake8 .

black:
	poetry run black .

black-check:
	poetry run black --check .

isort:
	poetry run isort .

isort-check:
	poetry run isort --check .

check: black-check isort-check flake8 types test

deps:
	poetry env use $(PYTHON)
	poetry install --all-extras --no-root

deps-lock:
	poetry lock --no-update

deps-sync:
	poetry install --all-extras --no-root --sync --with "dev"

deps-update:
	poetry lock

deps-tree:
	poetry show --tree
