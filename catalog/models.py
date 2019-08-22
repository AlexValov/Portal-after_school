from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse
from transliterate import translit
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class GeneralCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    general_category = models.ForeignKey(GeneralCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_view', kwargs={'slug': self.slug})

def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.name), reversed=True))
        instance.slug = slug

pre_save.connect(pre_save_category_slug, sender=Category)



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

class AgeFrom(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

class Tng(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Категория:')
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название:')
    gender = models.ForeignKey(Gender, on_delete=True, verbose_name='Возраст:')
    age_from  = models.ForeignKey(AgeFrom, on_delete=models.CASCADE, verbose_name='Со скольки лет:')
    # age_up = models.IntegerField(blank=True, db_index=True, verbose_name='До скольки лет:')
    description = models.TextField(db_index=True, verbose_name='Описание:')
    image = models.ImageField(upload_to='tng_images/', blank=False, db_index=True, verbose_name='Картинка:')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город:')
    company = models.CharField(max_length=100, db_index=True, verbose_name='Организация:')
    adress = models.CharField(max_length=100, db_index=True, verbose_name='Адрес:')
    phone = models.CharField(max_length=100, verbose_name='Телефон:')
    website =  models.CharField(blank=True, max_length=100, verbose_name='Сайт:')
    email = models.EmailField(verbose_name='Почта:')
    price = models.CharField(default='Бесплатно', max_length=50, verbose_name='Цена:')
    # slug = models.SlugField(blank=True, unique=True)
    slug = AutoSlugField(blank=True, populate_from='title', unique=True)
    available = models.BooleanField(default=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('training_view', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

#сортировка по дате публикации
    class Meta:
        ordering=['-date_pub']


def pre_save_tng_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.title), 'ru', reversed=True))
        instance.slug = slug
pre_save.connect(pre_save_tng_slug, sender=Tng)

