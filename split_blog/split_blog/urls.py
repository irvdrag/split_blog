from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # para login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  # ✅ incluye las rutas de tu app user
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # ✅ vista de login
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),# (X) vista de logout
    path('post/', include('post.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)