from django.shortcuts import render

def showdemopage(request):
    return render(request,"demo.html")
