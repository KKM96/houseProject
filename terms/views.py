from django.shortcuts import render
from .models import Question

# Create your views here.
def terms(request):
    return render(request, 'house/terms.html')

def terms(request):
    """
    terms 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'house/terms.html', context)