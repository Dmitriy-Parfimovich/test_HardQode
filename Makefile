migrate:
	poetry run python manage.py migrate

start:
	poetry run python manage.py runserver 0.0.0.0:8000

lint:
	poetry run flake8 .