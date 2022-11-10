from django.apps import AppConfig


class LouslistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'louslist'

    def ready(self):
        import louslist.signals
