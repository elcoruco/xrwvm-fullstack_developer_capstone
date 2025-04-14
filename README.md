# coding-project-template

## Install from scratch

```bash
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate

python3 -m pip install -U -r requirements.txt 

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
