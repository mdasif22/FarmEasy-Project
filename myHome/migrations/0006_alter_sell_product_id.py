# Generated by Django 4.1.7 on 2023-03-25 17:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myHome', '0005_sell_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell_product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
