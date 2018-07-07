# Dev local

dev.virtualenv:
	virtualenv _venv

dev.install:
	pip install -r requirements-dev.txt
	pip install -e .

dev.build:
	rm -rf ./dist
	rm -rf ./Chiplotle.egg-info
	python setup.py sdist

dev.test:
	tox -r

dev.push:
	twine upload -r pypi dist/Chiplotle-*.tar.gz

# Docs

docs.build:
	cd chiplotle/documentation && make html && cd -

