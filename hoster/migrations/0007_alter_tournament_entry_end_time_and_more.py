# Generated by Django 4.1.6 on 2023-02-11 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoster', '0006_team_teams_tournament'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='entry_end_time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='start_time',
            field=models.TimeField(blank=True),
        ),
    ]
