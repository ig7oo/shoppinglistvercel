from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']

    def clean_email(self):
        # Hämta e-postadressen från den rensade formulärdatan
        email = self.cleaned_data.get('email')
        # Kontrollera om en användare med denna e-postadress redan finns i databasen
        if User.objects.filter(email=email).exists():
            # Om e-postadressen finns, generera ett valideringsfel
            raise forms.ValidationError('This email already exists.')
        # Returnera den validerade e-postadressen om den är unik
        return email