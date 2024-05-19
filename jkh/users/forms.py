from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ('last_name', 'first_name', 'patronymic', 'email')


class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'patronymic', 'email', 'gas_account',
                  'electricity_account', 'water_account')
        exclude = ('password',)


# class UserUpdateForm(forms.ModelForm):
#     username = forms.CharField(
#         validators=[UnicodeUsernameValidator()],
#         label='Имя пользователя',
#         widget=MaterialTextInput(
#             help_text='Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
#             persistent_help_text=True,
#            ),
#        )
#
#     class Meta:
#         model = User
#         fields = ('username',)
