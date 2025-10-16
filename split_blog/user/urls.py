from django.urls import path
from .views import  ProfileView, ProfileUpdateView,RegisterView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('perfil/', ProfileView.as_view(), name='profile'),
    path('perfil/editar/', ProfileUpdateView.as_view(), name='edit_profile'),
]