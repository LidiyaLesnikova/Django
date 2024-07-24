import random
import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Client, Product, Order, Count

def index(request):
    return render(request, 'base.html')

def read_clients(request):
    list_clients = Client.objects.all()
    context = {'list_clients': list_clients}
    return render(request, 'thirdapp/clients.html', context)

def read_products(request):
    if request.method == 'POST':
        days_report=request.POST.get('days_report')
        client_id=request.POST['client_id']
        start_data_report = datetime.datetime.today() - datetime.timedelta(days=int(days_report))
        select_order = Order.objects.filter(
            client = client_id,
            date_ordered__gte=start_data_report,
            date_ordered__lt=datetime.datetime.today())
        list_products = set()
        for products in select_order:
            for product in products.product.all():
                list_products.add(product)
        print_client = f" клиента {Client.objects.filter(id=client_id).first().name}"
    else:
        list_products = Product.objects.all()
        print_client = ""
    context = {'list_products': list_products, 'print_client': print_client}
    return render(request, 'thirdapp/products.html', context)

def read_orders(request):
    list_orders = Order.objects.all()
    context = {'list_orders': list_orders}
    return render(request, 'thirdapp/orders.html', context)

def create_client(request):
    if request.method == 'POST':
        return  render(request, 'thirdapp/client.html')

def register_client(request):
    if request.method == 'POST':
        new_client = Client(name=request.POST['name'], 
                            email=request.POST['email'], 
                            phonenumber=request.POST['phonenumber'],
                            adress=request.POST['adress'])
        new_client.save()
    return HttpResponseRedirect('/clients/')

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

def update(request):
    return HttpResponse('Обновление записей интернет-магазина')

def delete_all(request):
    Client.objects.all().delete()
    Product.objects.all().delete()
    Order.objects.all().delete()
    return HttpResponse('Все записи БД удалены')
