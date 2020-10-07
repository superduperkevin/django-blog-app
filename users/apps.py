from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):    #added to meet django importing rules
        import users.signals