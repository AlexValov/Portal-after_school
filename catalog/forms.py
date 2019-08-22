from django.contrib.auth.models import User
from django import forms
from catalog.models import Tng

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    username.widget.attrs.update({'class': 'form-control'}),
    password.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email' )
        widgets={
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserFormEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)

    email.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'})
        }

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Tng
        fields = ('subcategory', 'title', 'gender', 'age_from', 'description', 'image', 'company', 'city', 'adress', 'phone', 'website', 'email', 'price')
        widgets={
            'subcategory': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age_from': forms.Select(attrs={'class': 'form-control'}),
            # 'age_up': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'})
        }






