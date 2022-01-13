
#from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from polls import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('', RedirectView.as_view(url='/polls/agenda')),

    #path('', views.index),

]