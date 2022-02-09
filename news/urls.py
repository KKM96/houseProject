from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news, name='news'),
    path('/news_naver', views.news_naver, name='news_naver'),
    path('/news_daum', views.news_daum, name='news_daum'),
    path('/htsale', views.htsale, name='htsale'),
    path('/htmonth', views.htmonth, name='htmonth'),
    path('/htsub', views.htsub, name='htsub'),
]