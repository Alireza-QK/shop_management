from django.db import models
from ..account.models import User
from ..product.models import Product


class Order(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
	is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده', default=False)
	payment_date = models.DateTimeField(verbose_name='تاریخ پرداخت', blank=True, null=True)

	class Meta:
		verbose_name = 'سبد خرید'
		verbose_name_plural = 'سبد های خرید'

	def __str__(self):
		return self.owner.username


class OrderDetail(models.Model):
	order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='orderdetails', verbose_name='سبد خرید')
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products', verbose_name='محصول')
	price = models.IntegerField(verbose_name='قیمت محصول')

	class Meta:
		verbose_name = 'جزیئات محصول'
		verbose_name_plural = 'جزیئات محصولات'

	def __str__(self):
		return self.product.title
