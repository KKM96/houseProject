from django.shortcuts import render

# Create your views here.
def search(request):
    return render(request, 'house/search.html')