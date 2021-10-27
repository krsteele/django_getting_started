from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting


def welcome(request):
    """Handles an HTTP request for the welcome page of our website"""
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    """Handles an HTTP request for the about page of our website"""
    return HttpResponse("I'm Cat Sandwich and I love rainbow sprinkles on everything.")