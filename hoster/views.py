from math import ceil

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.template.context_processors import csrf
from django.views import View

from TourneyHoster import settings
from users.models import Profile
from .models import Tournament, TournamentAccess, Team
import random
from django.shortcuts import render
from .forms import CreateTournamentForm
from paypal.standard.forms import PayPalPaymentsForm
# Create your views here.


# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})

    def post(self, request, *args, **kwargs):
        profiles = Profile.objects.all()
        total_players = profiles.count()
        num_teams = total_players // 4 + (total_players % 4 > 0)
        teams = {}
        for i in range(1, num_teams + 1):
            teams[i] = []

        players = list(profiles)
        random.shuffle(players)

        for player in players:
            assigned = False
            team_num = 1
            while not assigned:
                if len(teams[team_num]) < 4:
                    player.team_number = team_num
                    player.save()
                    teams[team_num].append(player)
                    assigned = True
                else:
                    team_num += 1
                    if team_num > num_teams:
                        team_num = 1

        args = {}
        args.update(csrf(request))
        args['num_teams'] = num_teams
        args['players'] = players
        args['team_range'] = range(1, num_teams + 1)

        return render(request, 'index.html', args)

def tournaments_view(request):
    tournaments = Tournament.objects.all().order_by('-id')

    if request.user.is_authenticated:
        profile = request.user.profile
        for tournament in tournaments:
            entry = tournament.entry_fee
            if profile in tournament.profiles.all():
                pass

            # try:
            #     access = TournamentAccess.objects.get(tournament=tournament, profile=profile)
            #     if access.paid:
            #         user_has_paid = True
            #         break
            # except TournamentAccess.DoesNotExist:
            #     user_has_paid = False


    context = {
        'tournaments': tournaments,
        'profile': request.user.profile
    }
    return render(request, 'tournaments.html', context)

def tournament_detail_view(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    teams = Team.objects.filter(teams_tournament=tournament)
    subs = tournament.subs.all()

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": tournament.respins_fee,
        "item_name": tournament.name + " Respin",
        # "invoice": tournament_id,
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('randomize_teams', args=[tournament_id])),
        "cancel_return": request.build_absolute_uri(reverse('tournament_detail', args=[tournament_id])),
    }
    paypal_form = PayPalPaymentsForm(initial=paypal_dict)

    context = {
        'tournament': tournament,
        'teams': teams,
        'subs': subs,
        'paypal_form': paypal_form
    }
    return render(request, 'tournament_detail.html', context)

def randomize_teams_view(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    players = list(tournament.profiles.all())
    teams = Team.objects.filter(teams_tournament=tournament)

    # Clear existing teams and subs
    # tournament.teams.all().delete()
    tournament.subs.clear()
    for team in teams:
        team.players.clear()

    # Randomize the players
    random.shuffle(players)

    team_number = 1
    subs = []
    for i, player in enumerate(players):
        if i % 4 == 0:
            if len(subs) >= 4:
                team, created = Team.objects.get_or_create(teams_tournament=tournament, id=team_number)
                team.players.set(subs[:4])
                subs = subs[4:]
                team_number += 1
            else:
                team, created = Team.objects.get_or_create(teams_tournament=tournament, id=team_number)
                team_number += 1
        if created:
            team.players.add(player)
        else:
            if team.players.count() >= 4:
                subs.append(player)
            else:
                team.players.add(player)

    tournament.subs.set(subs)

    return redirect('tournament_detail', tournament_id=tournament_id)


# Admin Side
def create_tournament_view(request):
    if request.method == 'POST':
        form = CreateTournamentForm(request.POST)
        if form.is_valid():
            tournament = form.save()
            return redirect('tournament_details', tournament_id=tournament.id)
    else:
        form = CreateTournamentForm()

    context = {
        'form': form
    }

    return render(request, 'admin/create_tournament.html', context)


def tournament_payment_view(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": tournament.entry_fee,
        "item_name": tournament.name,
        "invoice": tournament_id,
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('tournament_payment_success', args=[tournament_id])),
        "cancel_return": request.build_absolute_uri(reverse('tournament_payment_cancel', args=[tournament_id])),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, "tournament_payment.html", {"form": form, "tournament": tournament})


def tournament_payment_success(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    TournamentAccess.objects.create(profile=request.user.profile, tournament=tournament)
    return redirect("tournament_detail", tournament_id=tournament_id)

def tournament_payment_cancel(request, tournament_id):

    return redirect("tournaments")