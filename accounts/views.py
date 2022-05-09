from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from accounts.models import *
from django.http import HttpResponse

def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        print(username , pwd)
        if username and pwd is not None:
            user = authenticate(request, username=username, password=pwd)
            if user is not None:
                login(request , user)
                return redirect('index')
    return render(request , 'accounts/loginPage.html')

def register(request):
    pass


def logoutPage(request):
    logout(request)
    return redirect("loginPage")
def ProfilePage(request,pk):
    #Find the profile assiciateed with this user id
    try:
        profile = Profile.objects.get(user__id=pk)
        params = {
            'profile':profile
        }
        return render(request, 'accounts/profilePage.html', params)
    except Exception as E:
        print(str(E))
        return HttpResponse("<h1>Could not process this request. Kindly login again.</h1>")


