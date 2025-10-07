install:
	conda create -n python-for-data-science-PAC1 python=3.10 -y && \
	conda activate python-for-data-science-PAC1 && \
	pip install -r requirements.txt