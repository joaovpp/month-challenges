from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
  }


# Create your views here.

def index(request):
  months = list(challenges.keys())
  
  return render(request, "challenges/index.html", {
    "months": months
  })


def monthly_challenge(request, month):
  if month in challenges:
    challenge_text = challenges[month]
    return render(request, "challenges/challenge.html", {
      "text": challenge_text,
      "month_name": month
    })
    #response_data = render_to_string("challenges/challenge.html")
    #return HttpResponse(response_data)
  else:
    response_data = render_to_string("404.html")
    return HttpResponseNotFound(response_data)


def monthly_challenge_by_number(request, month):
  months = list(challenges.keys())
  if month > len(months):
     response_data = render_to_string("404.html")
     return HttpResponseNotFound(response_data)
  
  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenges", args=[redirect_month]) # /challenges/month
  return HttpResponseRedirect(redirect_path)
