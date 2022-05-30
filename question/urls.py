from django.urls import path 
from . import views
urlpatterns = [
    path('' , views.questions, name='questionIndex'),
    path('question_detail/<str:pk>' , views.questions_detail, name='questions_detail'),
    path('newQuestion',views.newQuestion, name='newQuestion'),


    path('newTest', views.newTest , name='newTest'),
    path('allTest', views.allTest , name='allTest' ),
    path('nwInput/<str:pk>/', views.nwInput , name='nwInput'),
    path('thankyou', views.thankyou, name='thankyou'),

    path('viewentries/<str:pk>', views.viewentries , name='viewentries')
    path('viewcod/<str:pk>', views.viewcod, name='viewcod')

]