
#from django.conf.urls import url
#from django.contrib import admin
from django.urls import path
from polls import views, admin
from django.views.generic import RedirectView

urlpatterns = [

    #path('admin/', admin.site.urls),
    #path('', RedirectView.as_view(url='/polls/agenda/')),
    #path('', views.index),
]