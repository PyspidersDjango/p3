from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>Welcome To The Project</marquee>")

def home(request):
    return render(request,"first.html")

def second(request):
    return render(request,"directory/second.html")

def third(request):
    return render(request,"directory/third.html",context={'data':"Akshay",'name':"Rajappa"})

def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange']
    return render(request,"directory/fourth.html",{'fruits':fruits})

def fifth(request):
    return render(request,"directory/fifth.html",{'a':10,'b':5})

def urls_data(request,name):
    return HttpResponse("<h1>{}</h1>".format(name))

def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))
