from django.shortcuts import render
from .models import *


def testIndex(request):
    return render(request , 'test/index.html')