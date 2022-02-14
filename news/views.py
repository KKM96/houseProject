from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
def news(request):
    return render(request, 'house/news.html')

def news_naver(request):
    return render(request, 'news/news_naver.html')

def index(request):
    """
    pybo 목록출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

def news_daum(request):
    return render(request, 'news/news_daum.html')

def htsale(request):
    return render(request, 'news/htsale.html')

def htmonth(request):
    return render(request, 'news/htmonth.html')

def htsub(request):
    return render(request, 'news/htsub.html')