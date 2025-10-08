ENVNAME = uve-data-search-ai
PYTHONVER = 3.12.8

install:
	@echo "Installing dependencies..."
	conda create -n $(ENVNAME) python=$(PYTHONVER) -y
	conda activate $(ENVNAME) && pip install -r requirements.txt