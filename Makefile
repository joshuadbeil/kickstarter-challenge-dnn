.PHONY: setup
setup:
		pyenv local 3.9.8
		python -m venv .venv
		.venv/bin/python -m pip install --upgrade pip
    .venv/bin/python -m pip install --no-binary=h5py h5py
		.venv/bin/python -m pip install -r requirements.txt
