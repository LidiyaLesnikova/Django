from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product, Order

def index(request):
    return HttpResponse('Интернет-магазин')

def create_fake_bases(request):
    for i in range(10):
        new_client = Client(name=f'client{i}', 
                            email=f'cl{i}@mail.ru', 
                            phonenumber=f'+799988877{i}',
                            adress= 'adress')
        new_client.save()


    return HttpResponse(site)
