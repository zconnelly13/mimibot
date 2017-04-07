run:
	PYTHONPATH='..' python src/main.py

test:
	echo "" > .test.db
	MIMIBOT_TEST=1 PYTHONPATH='..' nosetests --nocapture

db:
	mkdir -p db 
	touch db/pickle.db
