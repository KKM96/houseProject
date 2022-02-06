from django.shortcuts import render

# Create your views here.
def qna(request):
    return render(request, 'house/qna.html')