from django.shortcuts import render
from . models import Course, Question

def home(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'home.html', context)
