from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
    address = models.CharField(max_length=500)
    date_registration = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Client: {self.name} (email: {self.email}, phone: {self.phonenumber},\nadress: {self.address})'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    date_addition = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True)
    def __str__(self):
        photo_str = ''
        if self.photo.name is not '':
            photo_str = f', photo - {self.photo}'
        return f'Product is {self.name} (price = {self.price}, remains = {self.quantity}{photo_str})'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through='Count') 
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        itog_str = ""
        for i in self.product.all():
            itog_str = itog_str+ i.__str__() + '\n'
        return f'Order is {self.id} for the amount of {self.total_price}\n{itog_str}'
    
class Count(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count_product = models.PositiveIntegerField(default=0)
    
    def save_order(self):
       self.count_product += 1
       return self.count_product
    
    def __str__(self):
        return f'count {self.product} = {self.count_product}'