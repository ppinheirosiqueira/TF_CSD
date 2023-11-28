from django.shortcuts import render

# Create your views here.

def home(request):
    variavel = False
    return render(request, "PID/home.html", {"variavel": variavel,})
