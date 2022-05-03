from django.urls import path 
from . import views
urlpatterns = [
    path('' , views.index , name='questionIndex'),
    path('questions/<str:pk>' , views.questions, name='questions')
]