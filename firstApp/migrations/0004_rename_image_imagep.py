# Generated by Django 4.0.1 on 2022-01-14 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0003_remove_image_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ImageP',
        ),
    ]