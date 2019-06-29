from django.contrib import admin
from .models import Category, SubCategory, Tng, Gender, City

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tng)
admin.site.register(City)
admin.site.register(Gender)