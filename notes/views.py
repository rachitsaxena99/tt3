from django.shortcuts import render
from notes.models import Subject
from .filters import *
from django.contrib.auth.decorators import login_required

@login_required(login_url="loginPage")
def index(request):
    subjects = Subject.objects.all()
    flag= False
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        subjects = Subject.objects.filter(name__contains=keyword)
        if not len(subjects):
            flag=True

    params = {
        'subjects':subjects,
        'allSubjects':Subject.objects.all(),
        'flag':flag,
    }
    return render(request,'notes/index.html',params)

@login_required(login_url="loginPage")
def searchResults(request):
    subject = Subject.objects.all().first()
    if request.method=='POST':
        input = request.POST.get('subject')

        subject = Subject.objects.get(name=input)
        print(subject)
    params = {
        'subject':subject,
        'subjects':Subject.objects.all()
    }
    return render(request , 'notes/search-result.html', params)

@login_required(login_url="loginPage")
def mainPage(request):
    subjects = Subject.objects.all()

    params = {
        'subjects': subjects,
        'subject':subjects.first(),

    }
    return render(request,'notes/notesPage.html',params)