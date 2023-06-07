from django.urls import path, include, re_path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('simpanbuku/', views.simpanbuku, name='simpanbuku'),
    path('editbuku/', views.editbuku, name='editbuku'),
    path('deletebuku/', views.deletebuku, name='deletebuku'),
    path('ambilbuku/', views.ambilbuku, name='ambilbuku'),
    ]