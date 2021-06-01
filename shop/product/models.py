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

	# ********** Section resize image ***********
	image = Image.open(instance.image)
	resized_image = image.resize((400, 400))
	fileName = "%s.%s" % (uuid4(), image.format)
	filePath = f"{settings.MEDIA_ROOT}/product/images/{fileName}"
	instance.thumbnail = f"product/images/{fileName}"
	resized_image.save(filePath)

	# ********** this section for remove old image ***************
	print(instance.pk)
	if instance.pk:
		try:
			old_product_image = Product.objects.get(pk=instance.pk).image
			old_product_thumbnail = Product.objects.get(pk=instance.pk).thumbnail
		except Product.DoesNotExist:
			return False

		new_product_image = instance.image
		new_product_thumbnail = instance.thumbnail
		print(new_product_image)
		print(new_product_thumbnail)
		if old_product_image and old_product_image.url != new_product_image.url and old_product_thumbnail \
			and old_product_thumbnail.url != new_product_thumbnail.url:
			os.remove(old_product_image.path)
			os.remove(old_product_thumbnail.path)

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

	if object_current:
		os.remove(object_current.images.path)


@receiver(pre_save, sender=GalleryProduct)
def pre_save_gallery_product(sender, instance, **kwargs):

	if instance.pk:
		try:
			old_gallery_image = GalleryProduct.objects.get(pk=instance.pk).images
		except GalleryProduct.DoesNotExist:
			return False

		new_gallery_image = instance.images
		if old_gallery_image and old_gallery_image.url != new_gallery_image.url:
			os.remove(old_gallery_image.path)
