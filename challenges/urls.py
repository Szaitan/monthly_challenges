from django.urls import path
from . import views

urlpatterns = [
    path("", views.monthly_challenges_all, name="month-challenges"),
    path("<int:month>", views.monthly_challenge_by_num),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]