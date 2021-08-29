from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home-page"),
    # dynamic url
    path("<int:month>", views.monthly_challenge_by_number, name="month-challenge-number"),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
