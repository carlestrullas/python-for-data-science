ENVNAME = python-for-data-science
PYTHONVER = 3.12.8

install:
	@echo "Installing dependencies..."
	conda create -n $(ENVNAME) python=$(PYTHONVER) -y
	conda activate $(ENVNAME) && pip install -r requirements.txt

docs:
	@echo "Building Sphinx HTML documentation..."
	conda activate $(ENVNAME) && sphinx-build -b html doc doc/_build/html
	@echo "Docs available at PAC4_carlestrullas/doc/_build/html/index.html"