from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def longboot(reqest):
    return HttpResponse('hello world')
    