import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("My first application")

def about(request):
    return HttpResponse("About me")
