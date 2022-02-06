from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def index(request):
    return render(request, 'house/index.html')

# def about(request):
#     return render(request, 'house/about.html')
#
# def post(request):
#     return render(request, 'house/post.html')
#
# def contact(request):
#     return render(request, 'house/contact.html')