from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import SignUp, PasswordChangeView, edit_profile


app_name = 'users'

urlpatterns = [
    path("login/", LoginView.as_view(
        template_name="users/login.html",
        redirect_authenticated_user=True
    ), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),

    path('password/change/',
         PasswordChangeView.as_view(),
         name='profile_change_password'),

    path('profile/change/', edit_profile, name='profile_change'),
]
