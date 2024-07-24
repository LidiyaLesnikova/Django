from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.read_clients, name='read_clients'),
    path('products/', views.read_products, name='read_products'),
    path('orders/', views.read_orders, name='read_orders'),
    path('clients/create_client/', views.create_client, name='create_client'),
    path('register_client/', views.register_client, name='register_client'),
    path('create_fake_bases/', views.create_fake_bases, name='create_fake_bases'),
    path('update/', views.update, name='update'),
    path('delete_all/', views.delete_all, name='delete_all'),
]
