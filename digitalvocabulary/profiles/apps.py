from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        from . import signals  # Import the signals module to ensure signal handlers are registered when the app is ready