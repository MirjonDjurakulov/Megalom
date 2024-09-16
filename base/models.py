from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    image = models.ImageField(upload_to='Images', blank=True, null=True, verbose_name='Изображения')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Categories'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price_buy = models.IntegerField(blank=True, null=True)
    price_sell = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


# Create your models here.
