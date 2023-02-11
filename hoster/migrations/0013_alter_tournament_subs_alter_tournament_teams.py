# Generated by Django 4.1.6 on 2023-02-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_team'),
        ('hoster', '0012_alter_team_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='subs',
            field=models.ManyToManyField(blank=True, related_name='subs', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='teams',
            field=models.ManyToManyField(blank=True, to='hoster.team'),
        ),
    ]