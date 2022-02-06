from django.urls import path
from . import views

app_name = 'qna'

urlpatterns = [
    path('', views.qna, name='qna'),
]