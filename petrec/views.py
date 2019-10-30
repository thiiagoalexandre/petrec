from django.shortcuts import render, redirect
from .form import AddDog


def home(request):
    return render(request, 'petrec/home.html')


def anuncio(request):
    return render(request, 'petrec/anuncio.html')


def cadastro(request):
    data = {}
    form = AddDog(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    data['form'] = form
    return render(request, 'peterec/cadastro.html', {'form': form})


