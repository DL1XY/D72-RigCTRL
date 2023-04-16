coverage:  ## Run tests with coverage
	coverage erase
	coverage run --include=src/* -m pytest -ra
	coverage report -m

test:  ## Run tests
	pytest -ra

deps:  ## Install dependencies
	pip install black coverage flake8 mypy pylint pytest tox
	
lint:  ## Lint and static-check
	flake8 src
	pylint src
	mypy src

deploy_log:
	buildozer android debug deploy run logcat

deploy:
	buildozer android debug deploy run

run:
	python src/main.py