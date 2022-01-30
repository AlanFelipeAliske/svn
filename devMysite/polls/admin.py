
from django.contrib import admin
from polls.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criação', 'usuario')
    list_filter = ('usuario', 'titulo')
    ordering = ('id', 'titulo')

admin.site.register(Evento, EventoAdmin)