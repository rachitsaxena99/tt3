from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from accounts.models import *
from django.http import HttpResponse
from question.models import Company
from article.models import Tag

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
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')

        if pwd1 == pwd2:
            User.objects.create_user(username , email , pwd1)
            user = authenticate(request , username=username , password=pwd1)
            if user is not None:
                login(request , user)

            return redirect('fillAboutUs', pk=user.id)
    return render(request, 'accounts/register.html')


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


def fillAboutUs(request,pk):
    profile =Profile.objects.get(user__id=pk)
    if request.method=='POST':
        about = request.POST.get('about')
        if about is not None:
            profile.about = about
            profile.save()
            return redirect('fillExperience',  pk=profile.id)
    params = {
        'profile':profile
    }
    return render(request , 'accounts/fillAboutUs.html', params)

def fillExperience(request,pk):
    profile = Profile.objects.get(user__id=pk)
    if request.method=='POST':
        print(request.POST.get('skills'))
    params = {
        'profile':profile,
        'tags':Tag.objects.all()
    }
    return render(request , 'accounts/fillExperience.html', params)


def newExperience(request ,pk):
    profile = Profile.objects.get(id=pk)

    if request.method == 'POST':
        experince = Experience.objects.create(
            company=request.POST.get('company'),
            startDate = request.POST.get('startDate'),
            endDate = request.POST.get('endDate'),
            designation=request.POST.get('designation'),
            user = request.user
        )
        profile.experience.add(experince)
        profile.save()
        experince.save()
        return redirect('fillExperience' , pk=pk)

def newSkill(request,pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        i = request.POST.get('skill')
        try:
            tag = Tag.objects.get(name=i)
        except:
            pass
        profile.skills.add(tag)
        profile.save()
    return redirect('fillExperience',pk=pk)


def removeExperience(request,p1,p2):
    profile = Profile.objects.get(id=p1)
    experience = Experience.objects.get(id=p2)
    profile.experience.remove(experience)
    profile.save()
    print('Donee')