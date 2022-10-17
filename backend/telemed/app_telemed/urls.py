from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registrar/medico/', views.registrar_medico, name='registrar_medico'),
    path('registrar/cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('logout', views.logout_view, name='logout')
]