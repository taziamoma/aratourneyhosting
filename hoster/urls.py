from django.urls import path, include
from . import views
from .views import tournaments_view, tournament_detail_view, create_tournament_view, tournament_payment_view, tournament_payment_success, tournament_payment_cancel, randomize_teams_view

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('tournament/', tournaments_view, name="tournaments"),
    path('tournament/<int:tournament_id>', tournament_detail_view, name="tournament_detail"),
    path('create_tournament/', create_tournament_view, name="create_tournament"),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('tournament/<int:tournament_id>/payment/', tournament_payment_view, name='tournament_payment'),
    path('tournament/<int:tournament_id>/payment/success/', tournament_payment_success, name='tournament_payment_success'),
    path('tournament/<int:tournament_id>/payment/cancel/', tournament_payment_cancel, name='tournament_payment_cancel'),
    path('respin/<int:tournament_id>/', randomize_teams_view, name='randomize_teams'),
]
