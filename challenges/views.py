from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

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
        # response_data = render_to_string("challenges/challenge.html")
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
    except KeyError:
        return HttpResponse(f"<h1>This {month} is not supported by page.</h1>")


def monthly_challenges_all(request):
    # My solution with using
    months = list(monthly_challenges.keys())
    print(months)
    display_list = ""
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        display_list += f"<li><a href='{month_path}'>{month}</a></li>"

    # response_data = [f"<li><a href={reverse('month-challenge', args=[key])}>{key}</a></li>" for key, values in monthly_challenges.items()]
    # display_list = f"<ul>{response_data}</ul>"
    return HttpResponse(display_list)
