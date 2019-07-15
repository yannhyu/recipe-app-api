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

# To test in browser
docker-compose up
chrome + modify header extension
127.0.0.1:8000/api/user/
+++++++++++++++++++++++++++++++

127.0.0.1:8000/api/user/create/
test@londonappdev.compose
Awesome1
Test Name
+++++++++++++++++++++++++++++++

api/user/token/
test@londonappdev.compose
Awesome1
{
    "token": "e4ebeea999a32a3dcd79026b97fc221c93a2d829"
}

update token in mod-header extension

+++++++++++++++++++++++++++++++
api/recipe
http://127.0.0.1:8000/api/recipe/ingredients/
Cabbage


docker-compose run --rm app sh -c "python manage.py makemigrations core"

enable image related media and static settings

docker-compose build


add recipe image feature in models

docker-compose run --rm app sh -c "python manage.py makemigrations core"
