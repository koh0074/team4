# Generated by Django 5.1.3 on 2024-11-17 11:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_bookmark_created_at_alter_bookmark_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bookmark',
            new_name='FestivalBookmark',
        ),
    ]
