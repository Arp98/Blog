from django.contrib.auth.forms import UserCreationForm
from .models import Account


class CreateUserForms(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForms, self).__init__(*args, **kwargs)

    class Meta:
        model = Account
        fields = ['username', 'password1', 'password2']
