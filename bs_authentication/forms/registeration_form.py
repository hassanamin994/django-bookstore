from django import forms

class RegisterationForm(forms.Form):

    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(),required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
