from django.shortcuts import render

# Create your views here.
def news(request):
    return render(request, 'house/news.html')

def news_naver(request):
    return render(request, 'news/news_naver.html')

def news_daum(request):
    return render(request, 'news/news_daum.html')

def htsale(request):
    return render(request, 'news/htsale.html')

def htmonth(request):
    return render(request, 'news/htmonth.html')

def htsub(request):
    return render(request, 'news/htsub.html')