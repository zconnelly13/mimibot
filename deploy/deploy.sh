#!/usr/bin/env bash

ssh deploy@207.154.208.23 'sudo service mimibot stop; cd /home/deploy/mimibot; git checkout master; git pull origin master; source venv/bin/activate; pip install -r requirements.txt; make db; sudo service mimibot start;'
