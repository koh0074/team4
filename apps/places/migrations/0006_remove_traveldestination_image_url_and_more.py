# Generated by Django 5.1.3 on 2024-11-15 13:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_bookmark_unique_together_bookmark_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traveldestination',
            name='image_url',
        ),
        migrations.AddField(
            model_name='traveldestination',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='travel_images/'),
        ),
        migrations.CreateModel(
            name='TravelBookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.traveldestination')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'destination')},
            },
        ),
    ]
