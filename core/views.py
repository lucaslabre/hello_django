from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, name, idade):
	return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(name, idade))
