from django.urls import path
from doubt import views
urlpatterns = [
    path('' , views.index , name = 'doubtIndex'),
    path('newDoubt' , views.newDoubt , name='newDoubt'),
    path('doubt/<str:pk>/' , views.doubt , name='doubt'),
    path('yourDoubts',views.yourDoubts,name='yourDoubts' ),
    path('newComment/<str:pk>/' , views.newComment , name='newComment'),
    path('newSubComment/<str:pk>/' , views.newSubComment , name = 'newSubComment'),
    path('allDoubts', views.allDoubts , name='allDoubts'),
    path('searchDoubt', views.searchDoubt , name='searchDoubt'),


    path('newTag', views.newTag , name='newTag')
]
