from django.views.generic import TemplateView,CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterForm
from .forms import UserProfileForm
from .models import Profile
from django.contrib.auth.models import User

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            profile = self.request.user.profile
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=self.request.user)

        context['perfil'] = profile
        context['usuario'] = self.request.user
        context['page_title'] = "Tu perfil"
        return context
        
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UserProfileForm  # ✅ Usa el nuevo formulario
    template_name = 'user/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pasamos el usuario al formulario
        return kwargs

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, "✅ Perfil actualizado correctamente.")
        return super().form_valid(form)

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(
            user=user,
            birth_date=form.cleaned_data.get('birth_date'),
            avatar=form.cleaned_data.get('avatar'),
        )
        login(self.request, user)
        messages.success(self.request, "🎉 Registro exitoso. Bienvenido.")
        return super().form_valid(form)