from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community, name='community'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('answer/create/<int:post_id>/', views.answer_create, name='answer_create'),
    path('post/create/', views.post_create, name='post_create'),
    path('seoul/', views.seoul, name='seoul'),
    path('post/modify/<int:post_id>/', views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]