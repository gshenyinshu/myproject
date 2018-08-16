from django.shortcuts import render
#from django.http import HttpResponse
 

def index(request):
#    return HttpResponse("Hello,world!")
	return render(request, 'polls/index.html',{})

def layout(request):
	return render(request, 'polls/layout.html',{})


