from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','prenoms', 'email', 'password', 'niveau_etude', 'etablissement_origine', 'concours_souhaite']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nom'}),
            'prenoms': forms.TextInput(attrs={'placeholder': 'Prénoms'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),
            'niveau_etude': forms.TextInput(attrs={'placeholder': 'Niveau d\'étude'}),
            'etablissement_origine': forms.TextInput(attrs={'placeholder': 'Établissement d\'origine'}),
            'concours_souhaite': forms.TextInput(attrs={'placeholder': 'Concours souhaité'}),
        }
