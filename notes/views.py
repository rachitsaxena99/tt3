from django.shortcuts import render
from notes.models import Subject

def index(request):
    subjects = Subject.objects.all()
    params = {
        'subjects':subjects
    }
    return render(request,'notes/index.html',params)


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