# Generated by Django 4.1.7 on 2023-04-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myHome', '0012_sell_product_crop_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell_product',
            name='crop_img',
            field=models.ImageField(blank=True, default='veg1.jpeg', null=True, upload_to=''),
        ),
    ]
