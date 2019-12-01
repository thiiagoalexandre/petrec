from django.shortcuts import render, get_object_or_404
from .form import AddDog, AddUser
from .models import Usuario, Cachorro


def home(request):
    return render(request, 'petrec/home.html')


def anuncio(request):
    pet = Cachorro.objects.all().order_by('id')
    return render(request, 'petrec/anunciar/anuncio.html', {'pet': pet})


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
        Usuario.objects.create(nome=nome, cpf=cpf, telefone=telefone, email=email, senha=senha, )
        return render(request, 'petrec/home.html')
    else:
        return render(request, 'petrec/cadastro.html')


def anunciar(request):
    form = AddDog(request.POST or None)
    if form.is_valid():
        nome_c = request.POST.get('nome_c')
        descricao = request.POST.get('descricao')
        raca = request.POST.get('raca')
        local = request.POST.get('local')
        sexo = request.POST.get('sexo')
        recompensa = request.POST.get('recompensa')
        foto = request.FILES.get('foto')
        Cachorro.objects.create(nome_c=nome_c, descricao=descricao, raca=raca, local=local, sexo=sexo, recompensa=recompensa, foto=foto)
        return render(request, 'petrec/detalhe.html')  # criar pagina de view para o dog
    else:
        return render(request, 'petrec/cadastro_dog.html')


def detalhe(request):
    pet = Cachorro.objects.all().order_by('-nome_c')
    return render(request, 'petrec/datelhe.html', {'pet': pet})