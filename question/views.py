from django.shortcuts import render
from question.models import Category , Question

def index(request):
    cateogry  = Category.objects.all()
    params = {'cateogry':cateogry}
    return render(request, 'question/index.html' , params)


def questions(request, pk):
    category = Category.objects.get(id=pk)
    question = Question.objects.filter(tags__id=category.id)
    params = {'questions':question}
    return render(request, 'question/questions.html', params)


def questions_detail(request, pk):
    question = Question.objects.get(id=pk)
    paras = str(question.description).split('/')
    
    params = {
        'question':question,
        'paras':paras
    }
    return render(request, 'question/questions_detail.html', params)