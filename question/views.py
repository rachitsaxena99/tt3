from django.shortcuts import render
from question.models import Category , Question

def index(request):
    cateogry  = Category.objects.all()
    params = {'cateogry':cateogry}
    return render(request, 'question/index.html' , params)


def questions(request, pk):
    category = Category.objects.get(id=pk)
    question = Question.objects.filter(tags__in=[category])
    params = {'questions':questions}
    return render(request, 'question/questions.html', params)