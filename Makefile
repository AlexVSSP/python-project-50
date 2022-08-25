fast-check:
	poetry build
	python3 -m pip install --user --force-reinstall dist/*.whl