from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_fake_bases/', views.create_fake_bases, name='create_fake_bases'),
    path('read/', views.read, name='read'),
    path('update/', views.update, name='update'),
    path('delete_all/', views.delete_all, name='delete_all'),
]
