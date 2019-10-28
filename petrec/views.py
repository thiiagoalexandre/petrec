from django.shortcuts import render, HttpResponse


def home(request):
    return render(request,'home.html')

def anuncio(request):
    return render(request,'anuncio.html')
