ENVNAME = python-for-data-science-PAC1
PYTHONVER = 3.12.8

install:
	@echo "Installing dependencies..."
	conda create -n $(ENVNAME) python=$(PYTHONVER) -y
	call conda activate $(ENVNAME) && pip install -r requirements.txt