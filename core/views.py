from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, name, idade):
	if name == 'Thayna':
		return HttpResponse('<h1>{}, te amo meu amor <3</h1>'.format(name))
	return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(name, idade))
