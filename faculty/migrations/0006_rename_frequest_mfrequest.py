# Generated by Django 4.2.7 on 2023-12-15 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0005_rename_request_frequest'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='frequest',
            new_name='mfrequest',
        ),
    ]
