from django.urls import path
from doubt import views
urlpatterns = [
    path('' , views.index , name = 'doubtIndex'),
    path('newDoubt' , views.newDoubt , name='newDoubt'),
    path('doubt/<str:pk>/' , views.doubt , name='doubt'),
    path('newComment/<str:pk>/' , views.newComment , name='newComment'),
    path('newSubComment/<str:pk>/' , views.newSubComment , name = 'newSubComment')
]
