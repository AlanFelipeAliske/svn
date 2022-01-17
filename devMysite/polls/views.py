
from polls.models import Evento
from django.shortcuts import render, redirect
from django.http import HttpResponse


#def index(request):
#    return redirect('/polls/agenda/')

def lista_eventos(request):
    #usuario = request.user
    evento = Evento.objects.all()    #filter(usuario=usuario)
    dados = {'eventos' :evento}
    return render(request, 'agenda.html', dados)
