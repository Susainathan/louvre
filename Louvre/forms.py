from django import forms
from .models import Registeron
from . models import Ticket

class registerForm(forms.ModelForm):
    class Meta:
        model=Registeron
        fields="__all__"
        widgets={
            'Name':forms.TextInput(attrs={'class':'un','type':'text','placeholder':'Enter Name'}),
            'Email':forms.TextInput(attrs={'class':'un','type':'text','placeholder':'Enter Email ID'}),
            'City':forms.TextInput(attrs={'class':'un','type':'text','placeholder':'Enter City'}),
            'Country':forms.TextInput(attrs={'class':'un','type':'text','placeholder':'Enter Country'}),
            'Username':forms.TextInput(attrs={'class':'un','type':'text','placeholder':'Set Username'}),
            'Password':forms.PasswordInput(attrs={'class':'un','type':'password','placeholder':'Set Password'})
        }
class signinForm(forms.ModelForm):
    class Meta:
        model=Registeron
        fields=('Username','Password')
        widgets={
            'Username': forms.TextInput(attrs={'class': 'un', 'type': 'text', 'placeholder': 'Enter Username'}),
            'Password': forms.PasswordInput(attrs={'class': 'un', 'type': 'password', 'placeholder': 'Enter Password'})
        }

class ticketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields="__all__"
        widgets={
            'Name': forms.TextInput(attrs={'class': 'un', 'type': 'text', 'placeholder': 'Enter Name'}),
            'Email': forms.TextInput(attrs={'class': 'un', 'type': 'text', 'placeholder': 'Enter Email ID'}),
            'Date':forms.DateInput(attrs={'type': 'date'}),
            'City': forms.TextInput(attrs={'class': 'un', 'type': 'text', 'placeholder': 'Enter City'}),
            'Country': forms.TextInput(attrs={'class': 'un', 'type': 'text', 'placeholder': 'Enter Country'}),
        }