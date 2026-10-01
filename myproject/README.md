# myproject

Django full-stack app (backend + frontend in one project).

## Run locally
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser   # optional, for /admin/
    python manage.py runserver

Open http://127.0.0.1:8000/

## Structure
- `app/models.py, views.py, forms.py, urls.py`  -> backend
- `app/templates/app/`                          -> HTML pages
- `app/static/app/style.css, app.js`            -> CSS + JavaScript
- JSON API: `/api/items/`

## Deploy on Render
Build Command: `./build.sh`
Start Command: `gunicorn myproject.wsgi`
Env vars: `SECRET_KEY`, `DEBUG=False`, `DATABASE_URL`
