from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse
from transliterate import translit

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_view', kwargs={'slug': self.slug})

def pre_save_subcategory_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.name), reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_subcategory_slug, sender=SubCategory)


class City(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Tng(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Категория:')
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название:')
    gender = models.ForeignKey(Gender, on_delete=True, verbose_name='Возраст:')
    age_from  = models.IntegerField(db_index=True, verbose_name='Со скольки лет:')
    age_up = models.IntegerField(blank=True, db_index=True, verbose_name='До скольки лет:')
    description = models.TextField(db_index=True, verbose_name='Описание:')
    image = models.ImageField(upload_to='tng_images/', blank=False, db_index=True, verbose_name='Картинка:')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город:')
    company = models.CharField(max_length=100, db_index=True, verbose_name='Организация:')
    adress = models.CharField(max_length=100, db_index=True, verbose_name='Адрес:')
    phone = models.CharField(max_length=100, verbose_name='Телефон:')
    website =  models.CharField(blank=True, max_length=100, verbose_name='Сайт:')
    email = models.EmailField(verbose_name='Почта:')
    price = models.CharField(default='Бесплатно', max_length=50, verbose_name='Цена:')
    slug = models.SlugField(blank=True, unique=True)
    available = models.BooleanField(default=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('training_view', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

def pre_save_tng_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.title), reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_tng_slug, sender=Tng)

