.PHONY:	runserver
runserver:
	python3 manage.py runserver

.PHONY:	check
check:
	python3 manage.py check