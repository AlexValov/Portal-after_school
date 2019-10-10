from django.contrib import admin
from django.urls import path, include
from catalog import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView


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
    path('catalog/catalog/<str:slug>/', views.category_view, name='category_view'),
    path('catalog/training/<str:slug>/', views.training_view, name='training_view'),
    path('catalog/training_add/', views.add_training, name='add_training'),
    path('catalog/<str:slug>/edit/', views.training_edit, name='training_edit'),
    path('catalog/<str:slug>/delete/', views.training_delete, name='training_delete'),
    path('catalog/about_us/', views.about_us, name='about_us'),
    path('catalog/advertising/', views.advertising, name='advertising'),
    path('catalog/contacts/', views.contacts, name='contacts')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]
