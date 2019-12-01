"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from petrec.views import home, anuncio, cadastro, login, anunciar, detalhe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('anunciar/anuncio', anuncio, name='anuncio'),
    path('anunciar/detalhe/<slug.id>', detalhe, name='detalhe'),
    path('cadastro/', cadastro, name='cadastro'),
    path('anunciar/', anunciar, name='anunciar'),
    path('login/', login, name='login'),

]
