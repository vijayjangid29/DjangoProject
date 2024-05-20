from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from .models import Customer


class LoginForm (AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class CustomerRegistrationForm(UserCreationForm):
    username  = forms.CharField(label='Naam bol re', widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    email     = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'})) 
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'})) 
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password1 = cleaned_data.get('password1')
    #     password2 = cleaned_data.get('password2')

    #     if password1 != password2:
    #         raise ValidationError('Passwords do not match.')
        
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class Password_Change_form(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'autofocus': True,'autocomplete':'True' ,'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autofocus': True,'autocomplete':'True' ,'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'autofocus': True,'autocomplete':'True' ,'class': 'form-control'}))

class Rest_password_form (PasswordResetForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))


class set_password_form (SetPasswordForm):

    new_password1 = forms.CharField(label='New Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

    new_password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    











class CustomerProfileForm(forms.ModelForm):
   
    class Meta:
        model = Customer
        fields = ['name','locality','city','mobile','zipcode','state']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),

        }