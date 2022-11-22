from django.apps import AppConfig


class DjangoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangoapp'

def ready(self):
        from actstream import registry
        from . import signals
        registry.register(self.get_model('MyModel'))
