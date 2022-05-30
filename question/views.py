from django.shortcuts import render, redirect
from question.models import Category , Question
from .filters import QuestionFilter
from django.contrib.auth.decorators import login_required
from testroom.models import *
@login_required(login_url="loginPage")
def index(request):
    cateogry  = Category.objects.all()
    params = {'cateogry':cateogry}
    return render(request, 'question/index.html' , params)

@login_required(login_url="loginPage")
def questions(request):

    question = Question.objects.all()
    quesFilter = QuestionFilter(request.GET, queryset=question)
    question = quesFilter.qs
    print(question)

    params = {'questions':question,

              'quesFilter':quesFilter,
              'count':question.count()}
    return render(request, 'question/questions.html', params)

@login_required(login_url="loginPage")
def questions_detail(request, pk):
    question = Question.objects.get(id=pk)
    paras = str(question.description).split('/')
    
    params = {
        'question':question,
        'paras':paras
    }
    return render(request, 'question/questions_detail.html', params)

@login_required(login_url="loginPage")
def newQuestion(request):
    tags = Category.objects.all()
    if request.method=='POST':
        heading = request.POST.get('heading')
        desc = request.POST.get('description')
        tag = request.POST.get('selectTool')
        selectedTag = Category.objects.get(id=tag)
        question = Question.objects.create(
            heading=heading,
            description = desc,
            user = request.user,
            tags=selectedTag,

        )
        question.save()
        return redirect('questions_detail',pk=question.id)
    params ={
        'tags':tags
    }
    return render(request,'question/newQuestion.html',params)


def newTest(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        explaination = request.POST.get("explaination")
        endDate = request.POST.get("endDate")
        input = request.POST.get("input")
        output = request.POST.get('output')
        if heading and explaination and input and output and endDate is not None:
            test = Test.objects.create(user=request.user , deadline=endDate ,input=input, output=output, question= explaination , heading=heading)
            test.save()
            return  redirect('allTest')

    return render(request , 'question/newTest.html')

def allTest(request):
    questions = Test.objects.filter(status=True).order_by('-created_on')
    yourQus = Test.objects.filter(user=request.user)

    params = {
        'questions':questions,
        'yourQus':yourQus
    }
    return render(request , 'question/allTest.html', params)

def nwInput(request,pk):
    if request.method=='POST':
        input = request.POST.get('input')
        if input is not None:
            test = Test.objects.get(id=pk)
            case = TestCase.objects.create(user=request.user, code=input )
            test.entries.add(case)
            return redirect("thankyou")

    params = {
        'pk':pk,
        'test':Test.objects.get(id=pk)
    }
    return render(request, 'question/input.html',params)


def thankyou(request):
    return render(request , 'question/thankyou.html')


def viewentries(request, pk):
    tst= Test.objects.get(id=pk)
    params = {
        'entries':tst
    }
    return render(request, 'question/viewentries.html', params)

def viewcod(request):
    return render(request, '')