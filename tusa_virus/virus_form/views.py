from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Home file that will handle all home requests """
    return render(request, 'virus_form/home.html')


def about(request):
    return HttpResponse('<h1> Blog About</h1>')
# Create your views here.
