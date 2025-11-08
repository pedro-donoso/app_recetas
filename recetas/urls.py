from django.urls import path
from . import views

app_name = 'recetas'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('receta/<int:pk>/', views.detalle_receta, name='detalle_receta'),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/exito/', views.contacto_exito, name='contacto_exito'),
]