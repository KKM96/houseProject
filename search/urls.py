from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.search, name='search'),
    path('analysis/', views.analysis, name='analysis'),
    path('month_busan/', views.month_busan, name='month_busan'),
    path('month_daejeon/', views.month_daejeon, name='month_daejeon'),
    path('month_gyeonggi/', views.month_gyeonggi, name='month_gyeonggi'),
    path('month_incheon/', views.month_incheon, name='month_incheon'),
    path('month_seoul/', views.month_seoul, name='month_seoul'),
    path('sales/', views.sales, name='sales'),
    path('sell_busan/', views.sell_busan, name='sell_busan'),
    path('sell_daejeon/', views.sell_daejeon, name='sell_daejeon'),
    path('sell_gyeonggi/', views.sell_gyeonggi, name='sell_gyeonggi'),
    path('sell_incheon/', views.sell_incheon, name='sell_incheon'),
    path('sell_seoul/', views.sell_seoul, name='sell_seoul'),
]