from django.shortcuts import render
from .models import Region, MonthBusan, MonthIncheon, MonthDaejeon, MonthSeoul, MonthGyeonggi, SellDaejeon, SellSeoul, SellBusan, SellIncheon, SellGyeonggi
from django.core.paginator import Paginator
from django.db.models import Q, Count


# Create your views here.
def search(request):
    # 입력 parameter
    page = request.GET.get('page', '')
    kw = request.GET.get('kw', '')
    region1 = request.GET.get('region1')
    region2 = request.GET.get('region2')
    region3 = request.GET.get('region3')

    # data
    region_list = Region.objects.all()
    reg1_list = Region.objects.values_list("reg1", flat=True).distinct().order_by('reg1')
    reg2_list = Region.objects.values_list("reg2", flat=True).distinct().order_by('reg2')
    reg3_list = Region.objects.values_list("reg3", flat=True).distinct().order_by('reg3')
    month_busan_list = MonthBusan.objects.all()
    month_incheon_list = MonthIncheon.objects.all()
    month_daejeon_list = MonthDaejeon.objects.all()
    month_seoul_list = MonthSeoul.objects.all()
    month_gyeonggi_list = MonthGyeonggi.objects.all()

    #search
    if region1:
        reg2_list = region_list.filter(
            Q(reg1__startswith=region1)
        ).values_list("reg2", flat=True).distinct()

    if region2:
        reg3_list = region_list.filter(
            Q(reg2__startswith=region2)
        ).values_list("reg3", flat=True).distinct()

    if region3:
        month_busan_list = month_busan_list.filter(
            Q(dname__startswith=region3)
        ).distinct()
        month_gyeonggi_list = month_gyeonggi_list.filter(
            Q(dname__startswith=region3)
        ).distinct()
        month_incheon_list = month_incheon_list.filter(
            Q(dname__startswith=region3)
        ).distinct()
        month_daejeon_list = month_daejeon_list.filter(
            Q(dname__startswith=region3)
        ).distinct()
        month_seoul_list = month_seoul_list.filter(
            Q(dname__startswith=region3)
        ).distinct()

    #paginator
    paginator1 = Paginator(month_busan_list, 20)
    paginator2 = Paginator(month_seoul_list, 20)
    paginator3 = Paginator(month_daejeon_list, 20)
    paginator4 = Paginator(month_gyeonggi_list, 20)
    paginator5 = Paginator(month_incheon_list, 20)


    context = {
        'region_list':region_list,
        'reg1_list':reg1_list,
        'reg2_list':reg2_list,
        'reg3_list':reg3_list,
        'region1':region1,
        'region2':region2,
        'month_busan_list':month_busan_list,
        'month_incheon_list': month_incheon_list,
        'month_daejeon_list': month_daejeon_list,
        'month_gyeonggi_list': month_gyeonggi_list,
        'month_seoul_list':month_seoul_list,
        'kw':kw,
    }
    return render(request, 'house/search.html', context)


def month_busan(request):
    # 입력 parameter
    page = request.GET.get('page', '1')

    region1 = request.GET.get('region1')
    region2 = request.GET.get('region2')
    region3 = request.GET.get('region3')


    # data
    region_list = Region.objects.filter(reg1="부산광역시").all()
    reg2_list = Region.objects.filter(reg1="부산광역시").values_list("reg2", flat=True).distinct().order_by('reg2')
    reg3_list = Region.objects.filter(reg1="부산광역시").values_list("reg3", flat=True).distinct().order_by('reg3')
    month_busan_list = MonthBusan.objects.all()

    # search
    if region2:
        reg3_list = reg3_list.filter(reg2=region2).distinct()

    if region3:
        month_busan_list = month_busan_list.filter(dname=region3).distinct().order_by('bldg_nm')

    context = {
        'region_list': region_list,
        'reg2_list': reg2_list,
        'reg3_list': reg3_list,
        'region1': region1,
        'region2': region2,
        'month_busan_list': month_busan_list,
    }
    return render(request, 'search/month_busan.html', context)


def month_daejeon(request):
    # 입력 parameter
    page = request.GET.get('page', '1')

    region1 = request.GET.get('region1')
    region2 = request.GET.get('region2')
    region3 = request.GET.get('region3')


    # data
    region_list = Region.objects.filter(reg1="대전광역시").all()
    reg2_list = Region.objects.filter(reg1="대전광역시").values_list("reg2", flat=True).distinct().order_by('reg2')
    reg3_list = Region.objects.filter(reg1="대전광역시").values_list("reg3", flat=True).distinct().order_by('reg3')
    month_daejeon_list = MonthDaejeon.objects.all()

    # search
    if region2:
        reg3_list = reg3_list.filter(reg2=region2).distinct()

    if region3:
        month_daejeon_list = month_daejeon_list.filter(dname=region3).distinct().order_by('bldg_nm')

    context = {
        'region_list': region_list,
        'reg2_list': reg2_list,
        'reg3_list': reg3_list,
        'region1': region1,
        'region2': region2,
        'month_daejeon_list': month_daejeon_list,
    }
    return render(request, 'search/month_daejeon.html', context)


def month_gyeonggi(request):
    # 입력 parameter
    page = request.GET.get('page', '1')

    region1 = request.GET.get('region1')
    region2 = request.GET.get('region2')
    region3 = request.GET.get('region3')

    # data
    region_list = Region.objects.filter(reg1="경기도").all()
    reg2_list = Region.objects.filter(reg1="경기도").values_list("reg2", flat=True).distinct().order_by('reg2')
    reg3_list = Region.objects.filter(reg1="경기도").values_list("reg3", flat=True).distinct().order_by('reg3')
    month_gyeonggi_list = MonthGyeonggi.objects.all()

    # search
    if region2:
        reg3_list = reg3_list.filter(reg2=region2).distinct()

    if region3:
        month_gyeonggi_list = month_gyeonggi_list.filter(dname=region3).distinct().order_by('bldg_nm')

    context = {
        'region_list': region_list,
        'reg2_list': reg2_list,
        'reg3_list': reg3_list,
        'region1': region1,
        'region2': region2,
        'month_gyeonggi_list': month_gyeonggi_list,
    }
    return render(request, 'search/month_gyeonggi.html', context)


def month_incheon(request):
    # 입력 parameter
    page = request.GET.get('page', '1')

    region1 = request.GET.get('region1')
    region2 = request.GET.get('region2')
    region3 = request.GET.get('region3')

    # data
    region_list = Region.objects.filter(reg1="인천광역시").all()
    reg2_list = Region.objects.filter(reg1="인천광역시").values_list("reg2", flat=True).distinct().order_by('reg2')
    reg3_list = Region.objects.filter(reg1="인천광역시").values_list("reg3", flat=True).distinct().order_by('reg3')
    month_incheon_list = MonthIncheon.objects.all()

    # search
    if region2:
        reg3_list = reg3_list.filter(reg2=region2).distinct()

    if region3:
        month_incheon_list = month_incheon_list.filter(dname=region3).distinct().order_by('bldg_nm')

    context = {
        'region_list': region_list,
        'reg2_list': reg2_list,
        'reg3_list': reg3_list,
        'region1': region1,
        'region2': region2,
        'month_incheon_list': month_incheon_list,
    }
    return render(request, 'search/month_incheon.html', context)


def month_seoul(request):
    # 입력 parameter
    page = request.GET.get('page', '1')

    region1 = request.GET.get('region1')
    region2 = request.GET.get('region2')
    region3 = request.GET.get('region3')

    # data
    region_list = Region.objects.filter(reg1="서울특별시").all()
    reg2_list = Region.objects.filter(reg1="서울특별시").values_list("reg2", flat=True).distinct().order_by('reg2')
    reg3_list = Region.objects.filter(reg1="서울특별시").values_list("reg3", flat=True).distinct().order_by('reg3')
    month_seoul_list = MonthSeoul.objects.all()

    # search
    if region2:
        reg3_list = reg3_list.filter(reg2=region2).distinct()

    if region3:
        month_seoul_list = month_seoul_list.filter(dname=region3).distinct().order_by('bldg_nm')

    context = {
        'region_list': region_list,
        'reg2_list': reg2_list,
        'reg3_list': reg3_list,
        'region1': region1,
        'region2': region2,
        'month_seoul_list': month_seoul_list,
    }
    return render(request, 'search/month_seoul.html', context)


def sales(request):
    return render(request, 'search/sales.html')


def sell_busan(request):
    # 입력 parameter
    page = request.GET.get('page', '1')

    region1 = request.GET.get('region1')
    region2 = request.GET.get('region2')
    region3 = request.GET.get('region3')


    # data
    region_list = Region.objects.filter(reg1="부산광역시").all()
    reg2_list = Region.objects.filter(reg1="부산광역시").values_list("reg2", flat=True).distinct().order_by('reg2')
    reg3_list = Region.objects.filter(reg1="부산광역시").values_list("reg3", flat=True).distinct().order_by('reg3')
    sell_busan_list = SellBusan.objects.all()

    # search
    if region2:
        reg3_list = reg3_list.filter(reg2=region2).distinct()

    if region3:
        sell_busan_list = sell_busan_list.filter(dname=region3).distinct().order_by('bldg_nm')

    context = {
        'region_list': region_list,
        'reg2_list': reg2_list,
        'reg3_list': reg3_list,
        'region1': region1,
        'region2': region2,
        'sell_busan_list': sell_busan_list,
    }
    return render(request, 'search/sell_busan.html', context)


def sell_daejeon(request):
    # 입력 parameter
    page = request.GET.get('page', '1')

    region1 = request.GET.get('region1')
    region2 = request.GET.get('region2')
    region3 = request.GET.get('region3')


    # data
    region_list = Region.objects.filter(reg1="대전광역시").all()
    reg2_list = Region.objects.filter(reg1="대전광역시").values_list("reg2", flat=True).distinct().order_by('reg2')
    reg3_list = Region.objects.filter(reg1="대전광역시").values_list("reg3", flat=True).distinct().order_by('reg3')
    sell_daejeon_list = SellDaejeon.objects.all()

    # search
    if region2:
        reg3_list = reg3_list.filter(reg2=region2).distinct()

    if region3:
        sell_daejeon_list = sell_daejeon_list.filter(dname=region3).distinct().order_by('bldg_nm')

    context = {
        'region_list': region_list,
        'reg2_list': reg2_list,
        'reg3_list': reg3_list,
        'region1': region1,
        'region2': region2,
        'sell_daejeon_list': sell_daejeon_list,
    }
    return render(request, 'search/sell_daejeon.html', context)


def sell_gyeonggi(request):
    # 입력 parameter
    page = request.GET.get('page', '1')

    region1 = request.GET.get('region1')
    region2 = request.GET.get('region2')
    region3 = request.GET.get('region3')

    # data
    region_list = Region.objects.filter(reg1="경기도").all()
    reg2_list = Region.objects.filter(reg1="경기도").values_list("reg2", flat=True).distinct().order_by('reg2')
    reg3_list = Region.objects.filter(reg1="경기도").values_list("reg3", flat=True).distinct().order_by('reg3')
    sell_gyeonggi_list = SellGyeonggi.objects.all()

    # search
    if region2:
        reg3_list = reg3_list.filter(reg2=region2).distinct()

    if region3:
        sell_gyeonggi_list = sell_gyeonggi_list.filter(dname=region3).distinct().order_by('bldg_nm')

    context = {
        'region_list': region_list,
        'reg2_list': reg2_list,
        'reg3_list': reg3_list,
        'region1': region1,
        'region2': region2,
        'month_sell_list': sell_gyeonggi_list,
    }
    return render(request, 'search/sell_gyeonggi.html', context)


def sell_incheon(request):
    # 입력 parameter
    page = request.GET.get('page', '1')

    region1 = request.GET.get('region1')
    region2 = request.GET.get('region2')
    region3 = request.GET.get('region3')

    # data
    region_list = Region.objects.filter(reg1="인천광역시").all()
    reg2_list = Region.objects.filter(reg1="인천광역시").values_list("reg2", flat=True).distinct().order_by('reg2')
    reg3_list = Region.objects.filter(reg1="인천광역시").values_list("reg3", flat=True).distinct().order_by('reg3')
    sell_incheon_list = SellIncheon.objects.all()

    # search
    if region2:
        reg3_list = reg3_list.filter(reg2=region2).distinct()

    if region3:
        sell_incheon_list = sell_incheon_list.filter(dname=region3).distinct().order_by('bldg_nm')

    context = {
        'region_list': region_list,
        'reg2_list': reg2_list,
        'reg3_list': reg3_list,
        'region1': region1,
        'region2': region2,
        'sell_incheon_list': sell_incheon_list,
    }
    return render(request, 'search/month_incheon.html', context)


def sell_seoul(request):
    # 입력 parameter
    page = request.GET.get('page', '1')

    region1 = request.GET.get('region1')
    region2 = request.GET.get('region2')
    region3 = request.GET.get('region3')

    # data
    region_list = Region.objects.filter(reg1="서울특별시").all()
    reg2_list = Region.objects.filter(reg1="서울특별시").values_list("reg2", flat=True).distinct().order_by('reg2')
    reg3_list = Region.objects.filter(reg1="서울특별시").values_list("reg3", flat=True).distinct().order_by('reg3')
    sell_seoul_list = SellSeoul.objects.all()

    # search
    if region2:
        reg3_list = reg3_list.filter(reg2=region2).distinct()

    if region3:
        sell_seoul_list = sell_seoul_list.filter(dname=region3).distinct().order_by('bldg_nm')

    context = {
        'region_list': region_list,
        'reg2_list': reg2_list,
        'reg3_list': reg3_list,
        'region1': region1,
        'region2': region2,
        'sell_seoul_list': sell_seoul_list,
    }
    return render(request, 'search/sell_seoul.html', context)


def analysis(request):
    return render(request, 'search/analysis.html')