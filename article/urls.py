from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics , name='topics'),
    path('articles/<str:pk>', views.articles , name='articles'),
    path('article-detail/<str:pk>', views.article_detail, name='article_detail'),
    path('newComment/<str:pk>' , views.newComment , name='newComment')
]