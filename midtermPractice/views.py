from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, welcome to index")

def about(request):
    msg = "<h3>Email: jakebasa17@gmail.com</h3>"
    return HttpResponse(msg)

def details(request):
    context = {
        'name': 'Jake',
        'age' : 21,
        'friends': ['renz', 'vito', 'neil'],
    }

    return render(request, "details.html", context)