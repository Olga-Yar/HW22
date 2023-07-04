from django.db import models
from django.urls import reverse
from slugify import slugify


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name='наименование')
    about = models.TextField(blank=True, verbose_name='описание')
    image = models.ImageField(upload_to='Product/', verbose_name='превью')
    #category = models.CharField(max_length=300, verbose_name='категория')
    price_lot = models.IntegerField(verbose_name='цена за покупку')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_last_change = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.name}: {self.about}'

    class Meta:
        verbose_name = 'Продукция'


class Category(models.Model):
    name = models.CharField(max_length=300, verbose_name='наименование', db_index=True)
    about = models.TextField(blank=True, verbose_name='описание')

    def __str__(self):
        return f'{self.name}: {self.about}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='содержимое')
    image = models.ImageField(upload_to='Blog/', blank=True, verbose_name='превью')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_public = models.BooleanField(default=True, verbose_name='публикация')
    num_views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} - {self.is_public}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_item', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, null=True)
    version_number = models.FloatField(verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=True, verbose_name='активно')

    def __str__(self):
        return f'{self.version_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

