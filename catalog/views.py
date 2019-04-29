from django.shortcuts import render, redirect
from catalog.forms import UserForm, UserFormEdit
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render (request, 'index.html', {})

def sign_up(request):
    user_form = UserForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_user.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))
            return redirect(index)

    return render(request, 'registration/sign_up.html', {
        'user_form': user_form
    })


def account(request):
    user_form = UserFormEdit(instance=request.user)

    if request.method == "POST":
        user_form = UserFormEdit(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()

            return redirect(index)

    return render(request, 'registration/account.html', {
        'user_form': user_form
    })




