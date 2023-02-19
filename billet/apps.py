from django.apps import AppConfig
from djano.apps import AppConfig


class BilletConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'billet'


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'