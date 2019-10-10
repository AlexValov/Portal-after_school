from django.urls import path, include
from catalog import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Эта строка опциональна и будет добавлять url'ы только при DEBUG = True
urlpatterns += staticfiles_urlpatterns()
