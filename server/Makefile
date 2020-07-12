# Stand-alone Apps
setup: django_setup django_seed_db

django_setup:
	pip3 install -r requirements.txt

django_seed_db:
	python3 manage.py migrate
	python3 manage.py loaddata bookstore/fixtures/*.json

django_reset_db:
	rm -rf bookstore/migrations/000*.py
	rm -rf db.sqlite3
	python3 manage.py makemigrations
	python3 manage.py migrate
