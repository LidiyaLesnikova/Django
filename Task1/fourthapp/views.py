import random
import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models import Client, Product, Order, Count
from .forms import ClientCreateForm, ProductCreateForm

def index(request):
    return render(request, 'base.html')

def read_clients(request):
    list_clients = Client.objects.all()
    context = {'list_clients': list_clients}
    return render(request, 'fourthapp/clients.html', context)

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
    return render(request, 'fourthapp/products.html', context)

def read_orders(request):
    list_orders = Order.objects.all()
    context = {'list_orders': list_orders}
    return render(request, 'fourthapp/orders.html', context)

def create_client(request):
    if request.method == 'POST':
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            new_client = Client(name=form.cleaned_data['name'], 
                                email=form.cleaned_data['email'], 
                                phonenumber=form.cleaned_data['phonenumber'],
                                address=form.cleaned_data['address'])
            new_client.save()
            return HttpResponseRedirect('/clients/')
    else:
        form = ClientCreateForm()
        return  render(request, 'fourthapp/new_entry.html', {'form': form, 'title':'Ввод данных клиента'})    

def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            photo=form.cleaned_data['photo']
            new_product = Product(name=form.cleaned_data['name'], 
                                description=form.cleaned_data['description'], 
                                price=form.cleaned_data['price'],
                                quantity=form.cleaned_data['quantity'],
                                photo=photo)
            new_product.save()
            fs = FileSystemStorage()
            fs.save(photo.name, photo)
            return HttpResponseRedirect('/products/')
    else:
        form = ProductCreateForm()
        return  render(request, 'fourthapp/new_entry.html', {'form': form, 'title':'Ввод нового товара'})    

def create_fake_bases(request):
    for i in range(10):
        new_client = Client(name=f'client{i+1}', 
                            email=f'cl{i+1}@mail.ru', 
                            phonenumber=f'+799988877{i+1:02}',
                            address= 'address')
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
