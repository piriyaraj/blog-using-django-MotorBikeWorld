# Generated by Django 4.0.5 on 2022-06-22 12:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_rename_bikespost_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Bikepost',
        ),
    ]