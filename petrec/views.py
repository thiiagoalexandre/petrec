from django.shortcuts import render, redirect
from .form import AddDog, AddUser
from .models import Usuario, Cachorro



def home(request):
    return render(request, 'petrec/home.html')


def anuncio(request):
    return render(request, 'petrec/anuncio.html')


def login(request):
    return render(request, 'petrec/login.html')

def cadastro(request):
    form = AddUser(request.POST or None)
    if form.is_valid():
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        Usuario.objects.create(nome=nome,cpf=cpf,telefone=telefone, email=email,senha=senha,)
        return render(request, 'petrec/home.html')
    else:
        return render(request, 'petrec/cadastro.html')





def anunciar(request):
    print(request.POST)
    form = AddDog(request.POST or None)
    if form.is_valid():
        print('faffhusgh')
        nome_c = request.POST.get('nome_c')
        descricao = request.POST.get('descricao')
        raca = request.POST.get('raca')
        local = request.POST.get('local')
        sexo = request.POST.get('recompensa')
        # foto = request.POST.get('foto')
        Cachorro.objects.create(nome=nome_c, cpf=descricao, telefone=raca, email=local, senha=sexo, foto=foto)
        return render(request, 'petrec/home.html') #criar pagina de view para o dog
    else:
        return render(request, 'petrec/cadastro_dog.html')