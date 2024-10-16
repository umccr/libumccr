install:
	@pip install '.[test,dev]'
	@pre-commit install

all:
	@pip install '.[test,dev,all]'
	@pre-commit install

check:
	@pre-commit run --all-files

scan:
	@trufflehog --debug --only-verified git file://./ --since-commit main --branch HEAD --fail

deep: scan
	@ggshield secret scan repo .

baseline:
	@detect-secrets scan --exclude-files '^(yarn.lock|.yarn/|.local/|openapi/)' > .secrets.baseline

up:
	@docker compose up -d

down:
	@docker compose down

stop:
	@docker compose down

ps:
	@docker compose ps

pytest:
	@py.test --no-cov tests/

test:
	@py.test

unit:
	@python -m unittest

tox:
	@tox -vv

nose:
	@nose2 -vv

coverage:
	@coverage run --source=libumccr -m pytest tests/

.PHONY: local
local:
	@py.test --cov-report html:local/coverage --cov=libumccr tests/
	@py.test --cov-report xml:local/coverage.xml --cov=libumccr tests/

clean:
	@rm -rf build/
	@rm -rf libumccr.egg-info/

.PHONY: dist
dist: clean
	@python3 -m build

# Usage: make testpypi version=0.2.0
testpypi: dist/libumccr-$(version).tar.gz
	@python3 -m twine upload --repository testpypi dist/libumccr-$(version).tar.gz
	@python3 -m twine upload --repository testpypi dist/libumccr-$(version)-*.whl

pypi: dist/libumccr-$(version).tar.gz
	@python3 -m twine upload dist/libumccr-$(version).tar.gz
	@python3 -m twine upload dist/libumccr-$(version)-*.whl
