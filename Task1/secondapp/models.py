from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
    adress = models.CharField(max_length=500)
    date_registration = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Client: {self.name} (email: {self.email}, phone: {self.phonenumber},\nadress: {self.adress})'

class Product (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.DecimalField(max_digits=8, decimal_places=2)
    date_addition = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Product is {self.name} (price = {self.price})'

class Order (models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    products_id = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return f'Order is {self.id}' 