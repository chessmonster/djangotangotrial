from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {'boldmessage' : "big, round, juicy, smooth..."}
    return render(request, 'rango/index.html', context=context_dict)
    
def about(request):
	return HttpResponse("Rango says this the about page <a href='/rango'>index</a>")
