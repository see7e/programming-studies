.PHONY: setup

setup:
	@read -p "Type GH name: " gh_name; \
	echo "Cloning from: https://github.com/$$gh_name/django.git"; \
	cd $$HOME; \
	git clone https://github.com/$$gh_name/django.git || true; \
	cd $$HOME/django; \
	python3 -m venv $$HOME/.virtualenvs/djangodev; \
	. $$HOME/.virtualenvs/djangodev/bin/activate; \
	python -m pip install -e $$HOME/django/

test:
	. $$HOME/.virtualenvs/djangodev/bin/activate; \
	cd $$HOME/django/tests; \
	python -m pip install -r requirements/py3.txt; \
	./runtests.py
