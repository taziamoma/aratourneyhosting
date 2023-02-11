# Generated by Django 4.1.6 on 2023-02-10 23:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_paid_profile_paid'),
        ('hoster', '0004_tournamentaccess_tournament_profiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='entry_end_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='start_time',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournament',
            name='subs',
            field=models.ManyToManyField(related_name='subs', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('players', models.ManyToManyField(to='users.profile')),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='teams',
            field=models.ManyToManyField(to='hoster.team'),
        ),
    ]
