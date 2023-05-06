# Generated by Django 4.1.7 on 2023-04-03 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myHome', '0018_user_to_farmeasy_crop_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_to_farmeasy',
            name='crop_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
