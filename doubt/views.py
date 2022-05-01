from django.shortcuts import render,redirect
from doubt.models import Doubt , Comment , subComment

def index(request):
    return render(request ,'doubt/index.html')


def newDoubt(request):
    if request.method=='POST':
        kwargs = {}
        txt = request.POST.get('doubtText')

        if txt is not None:
            file = request.FILES.get('myfile')

            if file is not None:
                d1 = Doubt.objects.create(ques=txt , user = request.user , image=file)
                d1.save()
                return redirect('doubt' , pk=d1.id)
            else:
                d1 = Doubt.objects.create(ques=txt , user = request.user)
                d1.save()
                return redirect('doubt' , pk=d1.id)

    return render(request , 'doubt/doubt.html')

def doubt(request , pk):
    doubt = Doubt.objects.get(id=pk)
    params = {
        'doubt':doubt
    }
    return render(request , 'doubt/doubt.html' , params)


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