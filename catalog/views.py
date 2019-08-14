from django.shortcuts import render, redirect
from catalog.forms import UserForm, UserFormEdit, TrainingForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
import datetime
from catalog.models import GeneralCategory, Category, SubCategory, Tng, City
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    generalcategories = GeneralCategory.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    tng = Tng.objects.all()[:5]

    return render (request, 'index.html' ,{
        'generalcategories':  generalcategories,
        'categories': categories,
        'subcategories': subcategories,
        'tng': tng
    })

def search_query(request):
    search_query = request.GET.get('search', '')
    tng_of_category = Tng.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    # Когда перейду на постгресс нужно будет проверить учитывает регистр или нет
    return render(request, 'catalog/search_query.html', {
        'tng_of_category': tng_of_category

    })



def category_in_menu(request):
    generalcategories = GeneralCategory.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    return render (request, 'category_in_menu.html', {
        'generalcategories':  generalcategories,
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

def profile(request):
    return redirect(catalog_in_profile)


def catalog_in_profile(request):
    user_tng = Tng.objects.filter(author=request.user)
    return render(request, 'catalog/catalog_in_profile.html', {
        'user_tng': user_tng
    })


def training_view(request, slug):
    # training = Tng.objects.get(slug__iexact=slug)
    training = get_object_or_404(Tng, slug__iexact=slug)

    return render(request, 'catalog/training.html', {
        'training': training
    })

def category_view(request, slug):
    # category = SubCategory.objects.get(slug__iexact=slug)
    category = get_object_or_404(SubCategory, slug__iexact=slug)
    tng_of_category = category.tng_set.all()

    paginator = Paginator(tng_of_category, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    #если есть другие страницы то отображаем нумерацию
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url
    }

    return render(request, 'catalog/catalog.html', context = context)


def add_training(request):
    form = TrainingForm()
    if request.method == "POST":
        form = TrainingForm(request.POST, request.FILES)
        if form.is_valid():
            tng = form.save(commit=False)
            tng.author = request.user
            tng.save()
            return redirect(tng)
    return render(request, 'catalog/add_training.html', {
        'form': form
    })

def training_edit(request, slug):
    # training = Tng.objects.get(slug__iexact=slug)
    training = get_object_or_404(Tng, slug__iexact=slug)
    form = TrainingForm(instance=training)
    if request.method == "POST":
        form = TrainingForm(request.POST, request.FILES, instance=Tng.objects.get(slug__iexact=slug))
        if form.is_valid():
            tng = form.save()
            return redirect(catalog_in_profile)
    return render(request, 'catalog/add_training.html', {
        'form': form,
        'training': training
    })

def training_delete(request, slug):
    # training = Tng.objects.get(slug__iexact=slug)
    training = get_object_or_404(Tng, slug__iexact=slug)
    if request.method == "POST":
        training.delete()
        return redirect(catalog_in_profile)
    return render(request, 'catalog/training_delete.html', {
        'training': training
    })


def about_us(request):
    return render(request, 'footer/about_us.html')

def advertising(request):
    return render(request, 'footer/advertising.html')

def contacts(request):
    return render(request, 'footer/contacts.html')