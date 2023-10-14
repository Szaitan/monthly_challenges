from django.urls import path
from . import views

urlpatterns = [
    path("", views.monthly_challenges_all),
    path("<int:month>", views.monthly_challenge_by_num),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]