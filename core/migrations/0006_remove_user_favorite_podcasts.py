# Generated by Django 4.1.2 on 2022-10-27 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_category_title_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorite_podcasts',
        ),
    ]
