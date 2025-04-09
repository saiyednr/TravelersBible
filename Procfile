web: gunicorn abgfm.wsgi --log-file - 
#or works good with external database
web: python manage.py makemigrations && python manage.py migrate && gunicorn abgfm.wsgi
