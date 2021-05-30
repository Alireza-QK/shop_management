from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=254)
    text = models.TextField()
    amount = models.BigIntegerField(verbose_name='قیمت', default=0)
    discount = models.BigIntegerField(verbose_name='قیمت با تخفیف', default=0)
    image = models.ImageField(verbose_name='تصویر', upload_to='product/images/')
    stock_count = models.IntegerField(verbose_name='تعداد موجودی', default=1)
    sell_count = models.IntegerField(verbose_name='تعداد به فروش رفته', default=0)
