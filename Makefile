default: help

help:
	@echo help
	@echo install
	@echo virtualenv
	@echo dependencies
	@echo db
	@echo test
	@echo run

install: virtualenv dependencies db

virtualenv:
	virtualenv .

dependencies:
	. bin/activate; pip install -r deps.txt

db:
	sqlite3 database/rest-cron.db < database/rest-cron.sql

test:
	. bin/activate; nosetests

run:
	. bin/activate; python main.py
