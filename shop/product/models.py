from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete
from django.conf import settings
import os
from PIL import Image
from uuid import uuid4


class Product(models.Model):
	title = models.CharField(max_length=254, verbose_name='عنوام محصول')
	text = models.TextField(verbose_name='توضیحات محصول')
	price = models.BigIntegerField(verbose_name='قیمت', default=0)
	discount = models.BigIntegerField(verbose_name='قیمت با تخفیف', default=0)
	image = models.ImageField(verbose_name='تصویر', upload_to='product/images/')
	thumbnail = models.ImageField(upload_to='product/images/', blank=True, null=True)
	stock_count = models.IntegerField(verbose_name='تعداد موجودی', default=1)
	sell_count = models.IntegerField(verbose_name='تعداد به فروش رفته', default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'محصول'
		verbose_name_plural = 'محصولات'


class GalleryProduct(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='galleries')
	images = models.ImageField(verbose_name='تصویر', upload_to='product/galleries/')

	def __str__(self):
		return self.product.title

	class Meta:
		verbose_name = 'گالری'
		verbose_name_plural = 'گالری ها'


# *********************** Section for model Product ***********************
@receiver(pre_save, sender=Product)
def pre_save_product(sender, instance, **kwargs):
	image = Image.open(instance.image)
	resized_image = image.resize((400, 400))
	fileName = "%s.%s" % (uuid4(), image.format)
	filePath = f"{settings.MEDIA_ROOT}/product/images/{fileName}"
	instance.thumbnail = f"product/images/{fileName}"
	resized_image.save(filePath)


@receiver(pre_delete, sender=Product)
def pre_delete_product(sender, instance, **kwargs):
	object_current = sender.objects.get(pk=instance.pk)

	if object_current:
		os.remove(object_current.image.path)
		os.remove(object_current.thumbnail.path)


# *********************** Section for model GalleryProduct ***********************
@receiver(pre_delete, sender=GalleryProduct)
def pre_delete_gallery_product(sender, instance, **kwargs):
	object_current = sender.objects.get(pk=instance.pk)

	print(object_current.images)
