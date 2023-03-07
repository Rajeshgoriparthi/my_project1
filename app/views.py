from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pspk (request):
    return HttpResponse('<h1><marquee bgcolor="red">Babulake babu ma kalyan babu</marquee></h1>')