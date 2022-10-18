from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registrar/medico/', views.registrar_medico, name='registrar_medico'),
    path('registrar/cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('logout/', views.logout_view, name='logout'),
    path('registrar/consulta/', views.registrar_consulta, name='registrar_consulta'),
    path('aceitar/consulta/<int:consulta_id>', views.aceitar_consulta, name='aceitar_consulta'),
    path('negar/consulta/<int:consulta_id>', views.negar_consulta, name='negar_consulta')
]