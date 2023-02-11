from django.db import models
from users.models import Profile

# Create your models here.
class Team(models.Model):
    players = models.ManyToManyField(Profile, related_name="team_players")
    teams_tournament = models.ForeignKey("hoster.Tournament", on_delete=models.CASCADE, related_name='teamtournament')

    def __str__(self):
        return "Team " + str(self.id)

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    entry_fee = models.DecimalField(max_digits=6, decimal_places=2)
    respins_fee = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(blank=True)
    start_time = models.DateTimeField(blank=True)
    entry_end_time = models.DateTimeField(blank=True)
    respins_start_time = models.DateTimeField(blank=True)
    respins_end_time = models.DateTimeField(blank=True)
    profiles = models.ManyToManyField(Profile, through='TournamentAccess')
    teams = models.ManyToManyField(Team, blank=True)
    subs = models.ManyToManyField(Profile, related_name='subs', blank=True)

    class Meta:
        db_table = "Tournament"

    def __str__(self):
        return self.name

class TournamentAccess(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.tournament.name + " - " + str(self.profile)

