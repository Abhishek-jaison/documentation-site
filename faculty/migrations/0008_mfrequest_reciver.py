# Generated by Django 4.2.7 on 2024-01-30 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('faculty', '0007_mfrequest_checked_mfrequest_permitted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mfrequest',
            name='reciver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
