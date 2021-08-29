from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january" : "this is jan",
    "february" : "this is feb",
    "march" : "this is march",
    "april" : "this is april",
    "may" : "this is may",
    "june" : "this is june",
    "july" : "this is july",
    "august" : "this is august",
    "september" : "this is september",
    "october" : "this is october",
    "november" : "this is november",
    "december" : None,
}

def index(request):
    months = list(monthly_challenges.keys())
    context = {
        "month_index": months
    }
    return render(request, "challenges/index.html", context)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        context = {
            "month_challenge" : challenge_text,
            "this_month" : month
        }
        return render(request, "challenges/challenge.html", context)

        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
    except:
        raise Http404()
        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!!")

    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month])  # /challenges/january
    return HttpResponseRedirect(redirect_path)
    

