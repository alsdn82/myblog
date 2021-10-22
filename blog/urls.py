from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 127.0.0.1:8000/blog
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('post/create/', views.post_create, name='post_create'),

]