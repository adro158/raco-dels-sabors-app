from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_platos, name='lista_platos'),
    path('borrar_plato/<int:plato_id>/', views.borrar_plato, name='borrar_plato'),
    path('editar_plato/<int:plato_id>/', views.editar_plato, name='editar_plato'),
    path('nueva_prevision/', views.crear_prevision, name='crear_prevision'),
]