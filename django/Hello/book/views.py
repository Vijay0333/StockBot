from django.shortcuts import render , HttpResponse

# Create your views here.

def index(request):
    context ={
        "variable":" this is new here u can see",
        "variable1":"great"
    }
    return render(request,'index2.html' ,context)
    #return HttpResponse("This is our homepage")

def about(request):
    return render(request,'About.html')
        #return HttpResponse("this is about page")

def services(request):
    return render(request,'Market.html')
    #return HttpResponse("this is services page")
def Contect(request):
    return render(request,'Contect.html')
    #return HttpResponse("This is Contect detail")

def Sprise(request):
    return render(request,'SharePrise.html')

def Trade(request):
    return render(request,'Trade.html')
