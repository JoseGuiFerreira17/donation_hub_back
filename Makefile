prebuild:
	cp example.env .env
	cp example.db.env .db.env

create_network:
	docker network create --gateway 10.8.0.1 --subnet 10.8.0.0/16 donation_network

build:
	docker compose up --build

migrate:
	docker compose exec donation_django python manage.py migrate

makemigrations:
	docker compose exec donation_django python manage.py makemigrations

reset_migrations:
	docker compose exec donation_django find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "*/venv/*" -delete
	docker compose exec donation_django python manage.py makemigrations

delete_pycache:
	find . -path "*/__pycache__" | xargs rm -rf

test:
	docker compose exec donation_django python manage.py test

lint:
	black .
	flake8 . --extend-exclude=migrations,venv --max-line-length 88

runserver:
	docker compose up

freeze:
	pip freeze > requirements.txt
