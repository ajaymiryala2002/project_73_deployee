python manage.py migrate
python manage.py collectstatic --noinput
gunicorn project_deployee.wsgi:application
