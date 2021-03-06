
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descrição = models.TextField(blank=True, null=True)
    data_evento = models.DateField(verbose_name='Data do evento')
    data_criação = models.DateField(auto_now=True, verbose_name='Data da criação')
    hora_criacao = models.DateTimeField(auto_now=True, verbose_name='Hora')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%y')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%d-%m-%y')
