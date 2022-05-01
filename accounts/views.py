from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout


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