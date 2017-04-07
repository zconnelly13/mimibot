run:
	PYTHONPATH='..' python src/main.py

test:
	rm .test.db
	MIMIBOT_TEST=1 PYTHONPATH='..' nosetests --nocapture

db:
	mkdir -p db 

lint:
	flake8 src/ tests/
