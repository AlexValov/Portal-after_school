from django.contrib.auth.models import User
from django import forms
from catalog.models import Tng

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class UserFormEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Tng
        fields = ('subcategory', 'title', 'gender', 'age', 'description', 'image', 'city', 'adress', 'phone', 'website', 'email', 'price')







