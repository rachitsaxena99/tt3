from django.urls import path
from accounts import views


urlpatterns = [
    path('login' ,views.loginPage , name='loginPage' ),
    path('register' , views.register , name = 'register'),
    path('logout' , views.logoutPage ,name='logoutPagee'),
    path('profilePage/<str:pk>' , views.ProfilePage ,name='profilePage' ),
    path('fill-aboutus/<str:pk>', views.fillAboutUs, name='fillAboutUs'),
    path('fill-experience/<str:pk>' , views.fillExperience , name='fillExperience'),
    path('newExperience/<str:pk>',views.newExperience , name='newExperience' ),
    path('newSkill/<str:pk>', views.newSkill , name='newSkill')
]