# Generated by Django 4.2.3 on 2023-08-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0007_remove_like_is_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
