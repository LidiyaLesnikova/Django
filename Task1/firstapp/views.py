from datetime import date
import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8"/>
    <title>Start</title>
    </head>
    <body>
    <h1>My first application</h1>
    </body>
    </html>
    '''
    return HttpResponse(html)

def about(request):
    today = date.today()
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8"/>
    <title>About me</title>
    </head>
    <body>
    <h1>About me</h1>
    <p>today {today}</p><br>
    The weather is hot. The temperature is +40C'
    </body>
    </html>
    '''
    return HttpResponse(html)
