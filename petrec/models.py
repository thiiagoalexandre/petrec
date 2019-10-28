from django.db import models

# Create your models here.
class TB_Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=60)
    senha = models.CharField(max_length=100)



class TB_Cachorro(models.Model):
    nome_c = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500)
    raca = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    recompensa = models.CharField(max_length=10)