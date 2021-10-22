from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.forms import PostForm
from blog.models import Post


def index(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)
    #return HttpResponse("안녕하세요~ 블로그 페이지입니다.")

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)

# 포스트 등록
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'blog/post_form.html', context)