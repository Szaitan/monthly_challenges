from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "January": "January month!",
    "February": "february month!",
    "March": "march month!",
    "April": "april month!",
    "May": "may month!",
    "Jun": "jun month!",
    "July": "july month!",
    "August": "august month!",
    "September": "september month!",
    "October": "october month!",
    "November": "november month!",
    "December": "december month!",
}


def monthly_challenge_by_num(request, month):
    try:
        redirect_month = list(monthly_challenges.keys())[month-1]
    except IndexError:
        return HttpResponseNotFound(f"<h1>There is no data for {month} input</h1>")

    redirect_path = reverse("month-challenge", args=[redirect_month]) #Tworzy ścieżkę /challenges/miesiąc
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
    except KeyError:
        return HttpResponse(f"<h1>This {month} is not supported by page.</h1>")
    return HttpResponse(response_data)


def monthly_challenges_all(request):
    # My solution with using
    response_data = [f"<a href={reverse('month-challenge', args=[key])}><h1>{key}</h1></a>" for key, values in monthly_challenges.items()]
    return HttpResponse(response_data)
