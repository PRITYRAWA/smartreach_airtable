from django.apps import AppConfig

class SmartreachapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smartreachapi'

    def ready(self):
        import smartreach.updater as updater
        updater.start()

