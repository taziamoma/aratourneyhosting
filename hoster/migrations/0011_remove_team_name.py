# Generated by Django 4.1.6 on 2023-02-11 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoster', '0010_tournament_respins_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='name',
        ),
    ]