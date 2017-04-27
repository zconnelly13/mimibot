run:
	PYTHONPATH='..' python src/main.py

chat:
	PYTHONPATH='..' python src/chat.py

test:
	rm -f .test.db
	MIMIBOT_TEST=1 PYTHONPATH='..' nosetests --nocapture

db:
	mkdir -p db 

lint:
	flake8 src/ tests/
