install:
	@pip install '.[test,dev]'

all:
	@pip install '.[test,dev,all]'

unit:
	@py.test --no-cov tests/

test:
	@py.test

.PHONY: dist
dist:
	@python setup.py sdist bdist_wheel

# Usage: make testpypi version=0.2.0
testpypi: dist/libumccr-$(version).tar.gz
	@twine upload --repository testpypi --sign dist/libumccr-$(version)*

pypi: dist/libumccr-$(version).tar.gz
	@twine upload --sign dist/libumccr-$(version)*
