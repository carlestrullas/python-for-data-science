install:
	pip install -r requirements.txt

run:
	jupyter notebook CAT_PAC1.ipynb

test:
	pytest tests/