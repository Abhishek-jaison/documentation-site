# Generated by Django 4.2.7 on 2024-03-28 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0009_alter_mfrequest_reciver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mfrequest',
            old_name='permitted',
            new_name='approved',
        ),
        migrations.AddField(
            model_name='mfrequest',
            name='rejected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mfrequest',
            name='reverted',
            field=models.BooleanField(default=False),
        ),
    ]
