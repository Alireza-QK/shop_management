from django.db import models


class Product(models.Model):
	title = models.CharField(max_length=254, verbose_name='عنوام محصول')
	text = models.TextField(verbose_name='توضیحات محصول')
	price = models.BigIntegerField(verbose_name='قیمت', default=0)
	discount = models.BigIntegerField(verbose_name='قیمت با تخفیف', default=0)
	image = models.ImageField(verbose_name='تصویر', upload_to='product/images/')
	stock_count = models.IntegerField(verbose_name='تعداد موجودی', default=1)
	sell_count = models.IntegerField(verbose_name='تعداد به فروش رفته', default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class GalleryProduct(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='galleries')
	images = models.ImageField(verbose_name='تصویر', upload_to='product/galleries/')

	def __str__(self):
		return self.product.title
