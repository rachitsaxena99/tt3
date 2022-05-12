from django.shortcuts import render
from question.models import Category , Question
from .filters import QuestionFilter
from django.contrib.auth.decorators import login_required

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