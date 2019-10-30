from django.db import models

# Create your models here.
class TB_Usuario(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    telefone = models.CharField(max_length=11, blank=False)
    email = models.CharField(max_length=60, blank=False)
    senha = models.CharField(max_length=100, blank=False)



class TB_Cachorro(models.Model):
    nome_c = models.CharField(max_length=100, blank=False)
    descricao = models.CharField(max_length=500, blank=False)
    raca = models.CharField(max_length=100, blank=False)
    local = models.CharField(max_length=100, blank=False)
    sexo = models.CharField(max_length=1, blank=False)
    recompensa = models.CharField(max_length=10)
    foto = models.FileField(upload_to="media/%Y/%m/%d")