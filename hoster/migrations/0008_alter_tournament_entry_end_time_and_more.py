# Generated by Django 4.1.6 on 2023-02-11 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoster', '0007_alter_tournament_entry_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='entry_end_time',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='start_time',
            field=models.DateTimeField(blank=True),
        ),
    ]