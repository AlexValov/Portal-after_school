from django.shortcuts import render, redirect
from catalog.forms import UserForm, UserFormEdit, TrainingForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import datetime
from catalog.models import Category,SubCategory, Tng, Gender


# Create your views here.


def index(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    return render (request, 'index.html' ,{
        'categories': categories,
        'subcategories': subcategories
    })


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

def training_view(request, slug):
    training = Tng.objects.get(slug__iexact=slug)

    return render(request, 'catalog/training.html', {
        'training': training
    })

def category_view(request, slug):

    category = SubCategory.objects.get(slug__iexact=slug)
    tng_of_category = category.tng_set.all()

    return render(request, 'catalog/catalog.html', {
        'category': category,
        'tng_of_category': tng_of_category
    })



def add_training(request):
    form = TrainingForm()
    if request.method == "POST":
        form = TrainingForm(request.POST, request.FILES)
        if form.is_valid():
            tng = form.save(commit=False)
            tng.save()
            return redirect(index)


    return render(request, 'catalog/add_training.html', {
        'form': form
    })





