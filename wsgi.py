import os
from django.core.wsgi import get_wsgi_application

# Point Django to your settings file
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

application = get_wsgi_application()
