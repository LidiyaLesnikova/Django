from django.contrib import admin

from .models import Client, Product, Order, Count

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phonenumber', 'address']
    list_filter = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'photo']
    list_filter = ['name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'total_price']

class CountAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product_name', 'count_product']

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Count, CountAdmin)

