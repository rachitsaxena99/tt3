from django.shortcuts import render,redirect
from doubt.models import Doubt , Comment , subComment
from django.contrib.auth.decorators import login_required

@login_required(login_url="loginPage")
def index(request):
    doubts = Doubt.objects.all()
    params = {
        'doubts':doubts
    }
    print(doubts)
    return render(request ,'doubt/index.html', params)

@login_required(login_url="loginPage")
def newDoubt(request):
    print(Doubt.objects.all().first().id)
    if request.method == 'POST':
        doubt = Doubt.objects.create(
            heading=request.POST.get('heading'),
            ques = request.POST.get('ques'),
            image = request.POST.get('image'),
            user=request.user
        )
        doubt.save()

        return redirect("doubt",pk=doubt.id)
    return render(request , 'doubt/newDoubt.html')

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