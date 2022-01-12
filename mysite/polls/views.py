#from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2 style='text-align:center'> Hello, world. You're at the polls index. </h2>")