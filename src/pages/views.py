from django.shortcuts import render
from django.http import HttpResponse 

def home_view(request,*args,**kwargs):
	print(args,kwargs)
	print(request.user)
	#return HttpResponse("<h1>Hello World</h1>")
	return render (request, "home.html", {} )
def contact_view(*args, **kwargs):
	return HttpResponse("<h1>Contact View</h1>")