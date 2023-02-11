# Generated by Django 4.1.6 on 2023-02-11 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoster', '0012_alter_team_players'),
        ('users', '0005_remove_profile_team_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hoster.team'),
        ),
    ]
