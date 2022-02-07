"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from house import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('house/', include('house.urls')),
    path('news/', include('news.urls')),
    path('search/', include('search.urls')),
    path('terms/', include('terms.urls')),
    path('community/', include('community.urls')),
    path('qna/', include('qna.urls')),
    path('login/', include('login.urls')),
    path('', views.index, name='index'),  # / 페이지에 해당하는 urlpatterns
]
