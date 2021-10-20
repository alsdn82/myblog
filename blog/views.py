from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def index(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)
    #return HttpResponse("안녕하세요~ 블로그 페이지입니다.")
