from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petstagram.accounts'

    def ready(self):
        from petstagram.accounts.signals import create_profile
