
from polls.models import Evento
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#def index(request):
#    return redirect('/polls/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Senha ou usuario invalidos')
        return redirect('/')


@login_required(login_url = '/login/')

def lista_eventos(request):
    #usuario = request.user
    evento = Evento.objects.all()    #filter(usuario=usuario)
    dados = {'eventos' :evento}
    return render(request, 'agenda.html', dados)
