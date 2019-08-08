"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from catalog import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('catalog/search/', views.search_query, name='search_query'),
    path('catalog/sign-up/', views.sign_up, name='sign-up'),
    path('catalog/account/', views.account, name='account'),
    path('catalog/profile/', views.profile, name='profile'),
    path('catalog/category/', views.category_in_menu, name='category_in_menu'),
    path('catalog/catalog_in_profile/', views.catalog_in_profile, name='catalog_in_profile'),
    path('catalog/calalog/<str:slug>/', views.category_view, name='category_view'),
    path('catalog/training/<str:slug>/', views.training_view, name='training_view'),
    path('catalog/training_add/', views.add_training, name='add_training'),
    path('catalog/<str:slug>/edit/', views.training_edit, name='training_edit'),
    path('catalog/<str:slug>/delete/', views.training_delete, name='training_delete')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]
