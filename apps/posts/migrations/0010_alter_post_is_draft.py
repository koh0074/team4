# Generated by Django 5.1.3 on 2024-11-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_tag_created_at_post_is_draft_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]