# coding-project-template

## Install from scratch

```bash
pip install virtualenv
# if the permissions are a problem try:
# brew install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate

python3 -m pip install -U -r requirements.txt 

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

## Add super user on kubernetes

```bash
kubectl exec dealership-6fc696756b-l9jb -- \
  env DJANGO_SUPERUSER_USERNAME=root \
      DJANGO_SUPERUSER_EMAIL=el.coruco@gmail.com \
      DJANGO_SUPERUSER_PASSWORD=root \
  python manage.py createsuperuser --noinput
```
