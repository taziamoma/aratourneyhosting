# Generated by Django 4.1.6 on 2023-02-11 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_paid_profile_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='team_number',
        ),
    ]
