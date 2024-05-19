from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView as BasePasswordChangeView
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, FormView
from django.urls import reverse_lazy

from .forms import UserCreationForm, UserChangeForm

User = get_user_model()


class SignUp(CreateView):
    form_class = UserCreationForm
    # После успешной регистрации перенаправляем пользователя в личный кабинет.
    success_url = reverse_lazy('users:profile_change')
    template_name = 'users/signup.html'


class PasswordChangeView(BasePasswordChangeView):
    success_url = reverse_lazy('users:profile')
    form_class = SetPasswordForm
    success_message = 'Пароль успешно изменен'


# TODO: сделать адекватную вьюшку и выбрать одно из трех ниже (cbv или функия)
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены')
            return render(request, 'users/personal_account.html', context={'form': form})
        return render(request, 'users/personal_account.html', {'form': form})
    else:
        form = UserChangeForm(instance=request.user)
        context = {'form': form}
        return render(request, 'users/personal_account.html', context)


class UserChangeView(LoginRequiredMixin, FormView):
    template_name = 'users/personal_account.html'
    model = User
    form_class = UserChangeForm
    success_url = 'Данные успешно обновлены'

    def get(self, request, *args, **kwargs):
        return super(UserChangeView, self).get(request, *args, **kwargs)


class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'users/personal_account.html'