from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
monthly_challenges = {
    "january": "January month!",
    "february": "february month!",
    "march": "march month!",
    "april": "april month!",
    "may": "may month!",
    "jun": "jun month!",
    "july": "july month!",
    "august": "august month!",
    "september": "september month!",
    "october": "october month!",
    "november": "november month!",
    "december": "december month!",
}


def monthly_challenge_by_num(request, month):
    try:
        redirect_month = list(monthly_challenges.keys())[month-1]
        print(redirect_month)
    except IndexError:
        return HttpResponseNotFound(f"There is no data for {month} input")

    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        display = monthly_challenges[month]
    except KeyError:
        return HttpResponse(f"This {month} is not supported by page.")
    return HttpResponse(display)
