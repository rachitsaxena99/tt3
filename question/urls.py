from django.urls import path 
from . import views
urlpatterns = [
    path('' , views.questions, name='questionIndex'),
    path('question_detail/<str:pk>' , views.questions_detail, name='questions_detail'),
]