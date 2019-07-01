# recipe-app-api

# Useful commands one
docker-compose run app sh -c "django-admin.py startproject app ."

docker-compose run app sh -c "python manage.py test"

docker-compose run app sh -c "python manage.py test && flake8"

docker-compose run app sh -c "python manage.py startapp core"

docker-compose run app sh -c "python manage.py makemigrations core"

docker-compose run app sh -c "python manage.py test"

docker-compose up

docker-compose run --rm app sh -c "python manage.py startapp user"

docker-compose run --rm app sh -c "python manage.py test"

# Useful commands two

docker-compose run --rm app sh -c "python manage.py startapp recipe"

docker-compose run --rm app sh -c "python manage.py makemigrations"
