from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class SettingsForm(forms.Form):
    categories_count = forms.IntegerField(label="Ilość kategorii", min_value=1, max_value=10)
    excluded_categories = forms.MultipleChoiceField(
        choices=[
            ("category1", "Kategoria 1"),
            ("category2", "Kategoria 2"),
            # Dodaj więcej kategorii...
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
