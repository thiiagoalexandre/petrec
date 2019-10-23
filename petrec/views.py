from django.shortcuts import render, HttpResponse


def mensagem1(request):
    return HttpResponse('Bem vindo!! ')
