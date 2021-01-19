#archivo para crear nuestras rutas
from django.urls import path

#importamos las vistas
from . import views


app_name='book' #asignamos nombre al url
urlpatterns = [
    path('', views.index, name='index' ), #hacemos referencia a la vista index 
    path('add', views.index, name='add' ),
]
