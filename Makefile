run:
	PYTHONPATH='..' python src/main.py

test:
	PYTHONPATH='..' nosetests --nocapture
