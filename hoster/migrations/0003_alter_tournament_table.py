# Generated by Django 4.1.6 on 2023-02-09 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoster', '0002_remove_tournament_max_players_tournament_date'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tournament',
            table='Tournament',
        ),
    ]
