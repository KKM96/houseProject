from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Answer
from django.utils import timezone
from .forms import PostForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


def community(request):
    """게시글 목록 출력"""
    #입력인자
    page = request.GET.get('page', 1) #페이지
    kw = request.GET.get('kw', '') #검색어

    #조회
    post_list = Post.objects.order_by('-create_date') #작성일시 역순 출력
    if kw:
        post_list = post_list.filter(
            Q(subject__icontains=kw) | #제목검색
            Q(content__icontains=kw) | #내용검색
            Q(author__username__icontains=kw) | #질문글쓴이검색
            Q(answer__author__username__icontains=kw) #답변글쓴이검색
        ).distinct()

    #페이징 처리
    paginator = Paginator(post_list, 10) #페이지당 10개씩 보여 주기
    page_obj = paginator.get_page(page)

    context = {'post_list' : page_obj, 'page' : page, 'kw' : kw}
    return render(request, 'community/post_list.html', context)

def detail(request, post_id):
    """게시판 내용 출력"""
    post = get_object_or_404(Post, pk=post_id)
    context = {'post' : post}
    return render(request, 'community/post_detail.html', context)

@login_required(login_url='login:login')
def answer_create(request, post_id):
    """게시글 답변 등록"""
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.post = post
            answer.save()
            return redirect('community:detail', post_id=post.id)
    else:
        form = AnswerForm()
    context = {'post': post, 'form': form}
    return render(request, 'community/post_detail.html', context)

@login_required(login_url='login:login')
def post_create(request):
    """게시글 등록"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            post.save()
            return redirect('community:community')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'community/post_form.html', context)

def seoul(request):
    return render(request, 'community/seoul.html')

@login_required(login_url='login:login')
def post_modify(request, post_id):
    """게시판 수정"""
    post = get_object_or_404(Post, pk=post_id)

    if request.user != post.author: #request.user = 로그인한 유저. question.author = 질문 작성자
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('community:detail', post_id = post.id)

    if request.method == "POST": #자기자신의 페이지가 이미 있는 상황일 때 저장 버튼을 누르면 post방식
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community:detail', post_id=post.id) #답변 등록하는 페이지로 이동(현재 화면 유지)

    else:
        form = PostForm(instance=post)
    context = {'form' : form}
    return render(request, 'community/post_form.html', context) #답변 등록하는 페이지로 이동


@login_required(login_url = 'login:login')
def post_delete(request, post_id):
    """게시글 삭제 """
    post = get_object_or_404(Post, pk = post_id)
    if request.user != post.author: #request.user = 로그인한 유저. question.author = 질문 작성자
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('community:detail', post_id = post.id)

    post.delete()
    return redirect('community:community')

@login_required(login_url = 'login:login')
def answer_modify(request, answer_id):
    """답변 수정"""
    answer = get_object_or_404(Answer, pk = answer_id)
    if request.user != answer.author: #request.user = 로그인한 유저.
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('community:detail', post_id = answer.post.id)

    if request.method == "POST": #자기자신의 페이지가 이미 있는 상황일 때 저장 버튼을 누르면 post방식
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit = False)
            answer.author = request.user
            answer.save()
            return redirect('community:detail', post_id = answer.post_id)

    else:
        form = AnswerForm(instance = answer)

    context = {'answer' : answer, 'form' : form}
    return render(request, 'community/answer_form.html', context)

@login_required(login_url = 'login:login')
def answer_delete(request, answer_id):
    """답변 삭제"""
    answer = get_object_or_404(Answer, pk = answer_id)
    if request.user != answer.author: #request.user = 로그인한 유저.
        messages.error(request, '삭제 권한이 없습니다.')

    else:
        answer.delete()
    return redirect('community:detail', post_id = answer.post.id)