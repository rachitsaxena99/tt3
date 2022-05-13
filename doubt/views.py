from django.shortcuts import render,redirect
from doubt.models import Doubt , Comment , subComment
from django.contrib.auth.decorators import login_required
from question.models import Category
from .fitlers import *
@login_required(login_url="loginPage")
def index(request):
    doubts = Doubt.objects.all().order_by('-date')
    queryset = DoubtFilter(request.GET, queryset=doubts)
    doubts = queryset.qs
    category = Category.objects.all()

    l1 = []
    for i in range(len(doubts)):
        if i == 3:
            break
        else:
            l1.append(doubts[i])
    print(l1)
    params = {
        'doubts':l1,
        'queryset':queryset,
        'category':category
    }
    print(doubts)
    return render(request ,'doubt/index.html', params)

@login_required(login_url="loginPage")
def newDoubt(request):

    category = Category.objects.all()
    if request.method == 'POST':
        category = Category.objects.get(id=request.POST.get('category'))

        doubt = Doubt.objects.create(
            heading=request.POST.get('heading'),
            ques = request.POST.get('ques'),
            category = category,
            user=request.user
        )
        doubt.save()

        return redirect("doubt",pk=doubt.id)
    params ={
        'category':category
    }
    return render(request , 'doubt/newDoubt.html', params)

@login_required(login_url="loginPage")
def doubt(request , pk):
    doubt = Doubt.objects.get(id=pk)
    params = {
        'doubt':doubt
    }
    return render(request , 'doubt/doubt.html' , params)

@login_required(login_url="loginPage")
def newComment(request , pk):
    doubt = Doubt.objects.get(id=pk)
    if request.method == 'POST':
        body = request.POST.get('body')
        com = Comment.objects.create(body = body , user=request.user , doubt=doubt )
        com.save()
        doubt.comments.add(com)
        doubt.save()

        return redirect('doubt' , pk=doubt.id)

def newSubComment(request , pk):
    comm = Comment.objects.get(id=pk)
    if request.method == 'POST':
        body = request.POST.get('body')
        nw = subComment.objects.create(body=body , user = request.user , doubt=comm.doubt)
        nw.save()
        comm.subComment.add(nw)
        comm.save()
        return redirect('doubt' , pk=comm.doubt.id)

def yourDoubts(request):
    doubt = Doubt.objects.filter(user=request.user)

    params = {
        'doubts':doubt
    }
    return render(request,'doubt/yourDoubts.html',params)

def allDoubts(request):
    doubts = Doubt.objects.all().order_by('-date')

    params = {
        'doubts':doubts,

    }
    return render(request,'doubt/allDoubts.html', params )


def searchDoubt(request):
    doubt = Doubt.objects.all().order_by('-date')
    if request.method == 'POST':
        text = request.POST.get('text')
        doubt = Doubt.objects.filter(ques__contains=text)

    params = {
        'doubts':doubt
    }
    return render(request , 'doubt/search-results.html',params)