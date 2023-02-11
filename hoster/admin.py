from django.contrib import admin
from users.models import Profile
from .models import Tournament, TournamentAccess, Team

# Register your models here.
admin.site.register(Profile)
admin.site.register(Tournament)
admin.site.register(TournamentAccess)
admin.site.register(Team)