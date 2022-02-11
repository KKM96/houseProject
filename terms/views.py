from django.shortcuts import render
from .models import Terms
from django.core.paginator import Paginator
from django.db.models import Q, Count
# csv reading 용 import
import json
from django.views import View
from django.http import HttpResponse, JsonResponse
import csv
import pandas as pd


# Create your views here.
def terms(request):
    result = []
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    term_lists = Terms.objects.all()
    # 검색
    if kw:
        term_lists = term_lists.filter(
            Q(Term_name__icontains=kw) |
            Q(Term_def__icontains=kw)
        ).distinct()
    # 페이징 처리
    paginator = Paginator(term_lists, 10)
    page_obj = paginator.get_page(page)

    context = {'term_lists': page_obj, 'page':page, 'kw':kw }
    return render(request, 'house/terms.html', context)


