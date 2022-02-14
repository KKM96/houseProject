from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm, AnswerForm

def community(request):
    """게시글 목록 출력"""
    post_list = Post.objects.order_by('-create_date') #작성일시 역순 출력
    context = {'post_list' : post_list}
    return render(request, 'community/post_list.html', context)

def detail(request, post_id):
    """게시판 내용 출력"""
    post = get_object_or_404(Post, pk=post_id)
    context = {'post' : post}
    return render(request, 'community/post_detail.html', context)

def answer_create(request, post_id):
    """게시글 답변 등록"""
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.post = post
            answer.save()
            return redirect('community:detail', post_id=post.id)
    else:
        form = AnswerForm()
    context = {'post': post, 'form': form}
    return render(request, 'community/post_detail.html', context)

def post_create(request):
    """게시글 등록"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('community:community')
    else:
        form = PostForm()
    context = {'form' : form}
    return render(request, 'community/post_form.html', context)

def seoul(request):
    return render(request, 'community/seoul.html')