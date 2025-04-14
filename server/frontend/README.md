# README

## How to start the server from scratch

```bash
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate
python3 -m pip install -U -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
```

## How to start the server

```bash
python3 manage.py runserver
```


