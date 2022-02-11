from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.search, name='search'),
    path('analysis/', views.analysis, name='analysis'),
    path('month/', views.month, name='month'),
    path('sales/', views.sales, name='sales'),
]