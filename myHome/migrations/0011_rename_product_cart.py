# Generated by Django 4.1.7 on 2023-04-01 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_state_profile_state_remove_profile_username_and_more'),
        ('myHome', '0010_rename_owner_product_current_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Cart',
        ),
    ]
