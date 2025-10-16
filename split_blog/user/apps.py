from django.apps import AppConfig

class UserConfig(AppConfig):  
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'  # Asegúrate de que la carpeta de tu app se llama exactamente 'user'

    def ready(self):
        import user.signals  # Este debe coincidir con el nombre de la app