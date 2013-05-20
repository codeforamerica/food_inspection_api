venv-food: venv-food/bin/activate

venv-food/bin/activate: requirements.txt
	test -d venv-food || virtualenv --no-site-packages venv-food
	. venv-food/bin/activate; pip install -Ur requirements.txt
	touch venv-food/bin/activate
