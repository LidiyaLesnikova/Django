import random
from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product, Order, Count

def index(request):
    return HttpResponse('Интернет-магазин')

def create_fake_bases(request):
    for i in range(10):
        new_client = Client(name=f'client{i+1}', 
                            email=f'cl{i+1}@mail.ru', 
                            phonenumber=f'+799988877{i+1:02}',
                            adress= 'adress')
        new_client.save()
        new_product = Product(name=f'product{i+1}', 
                            description='description', 
                            price=i+100,
                            quantity=i+10)
        new_product.save()
    for i in range(random.randint(1, 50)):
        new_order = Order(client = Client.objects.get(id=random.randint(1, 10)))
        new_order.save()
        sum = 0
        for j in range(random.randint(1, 10)):
            product=Product.objects.get(id=random.randint(1, 10))
            if product.quantity>0:
                count_product = Count.objects.filter(product=product, order=new_order).first()
                if count_product is not None:
                    new_order.product.add(product)
                    count_product.count_product+=1
                    count_product.save()
                else:
                    new_order.product.add(product, through_defaults={"count_product": Count(product=product, order=new_order).save_order()})
                new_order.save()
                product.quantity -= 1
                product.save()
                sum+=product.price
        new_order.total_price = sum
        new_order.save()

    return HttpResponse('База заполнена')

def read(request):
    return HttpResponse('Чтение записей интернет-магазина')

def update(request):
    return HttpResponse('Обновление записей интернет-магазина')

def delete_all(request):
    Client.objects.all().delete()
    Product.objects.all().delete()
    Order.objects.all().delete()
    return HttpResponse('Все записи БД удалены')
