.PHONY: all docs test compile upload_to_pypi clean format


LIBRARY_DIR := chiplotle
SRC_FILES := $(shell find $(LIBRARY_DIR)) 
SRC_FILES += setup.py
TEST_FILES := $(shell find $(LIBRARY_DIR) -iname test*.py)

all: test

docs:
	$(MAKE) html -C docs 

test: compile
	tox

compile:
	python -m compileall $(LIBRARY_DIR) -j $$(nproc)

format:
	black $(LIBRARY_DIR)

flake8:
	flake8 $(LIBRARY_DIR)

dist: $(SRC_FILES) compile
	rm -rf dist
	python setup.py sdist

upload_to_pypi: dist
	twine upload dist/*

clean:
	rm -rf dist
