.PHONY: start run stop clean

start:
	python3 -m venv venv
	. venv/bin/activate
	python3 -m pip install -r requirments.txt
run:
	python3 -i ds.py
clean:
	rm -rf venv
