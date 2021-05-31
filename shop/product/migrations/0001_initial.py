# Generated by Django 3.2.3 on 2021-05-31 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, verbose_name='عنوام محصول')),
                ('text', models.TextField()),
                ('price', models.BigIntegerField(default=0, verbose_name='قیمت')),
                ('discount', models.BigIntegerField(default=0, verbose_name='قیمت با تخفیف')),
                ('image', models.ImageField(upload_to='product/images/', verbose_name='تصویر')),
                ('stock_count', models.IntegerField(default=1, verbose_name='تعداد موجودی')),
                ('sell_count', models.IntegerField(default=0, verbose_name='تعداد به فروش رفته')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='product/galleries/', verbose_name='تصویر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleries', to='product.product')),
            ],
        ),
    ]
