PYTHON=3.11.6

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=flake8_class_attributes_order --cov-report=xml

types:
	poetry run mypy .

style:
	poetry run flake8 .

check: style types test

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
