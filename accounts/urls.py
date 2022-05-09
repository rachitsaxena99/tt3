from django.urls import path
from accounts import views


urlpatterns = [
    path('login' ,views.loginPage , name='loginPage' ),
    path('register' , views.register , name = 'register'),
    path('logout' , views.logoutPage ,name='logoutPagee'),
    path('profilePage/<str:pk>' , views.ProfilePage ,name='profilePage' )
]