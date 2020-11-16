setup:
	python3 -m venv .venv

install:
	python3 -m pip install --upgrade pip
	pip install -r requirements.txt 

copies:
	./copies.sh	

assemble:
	python3 model_data_assembly.py

remove:
	./remove.sh

data: copies assemble remove

all: install data
