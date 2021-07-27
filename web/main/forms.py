from .models import Users
from django.forms import ModelForm, TextInput

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ["name", "mail"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type your Name'
            }),
            "mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type your E-mail'
            })
        }