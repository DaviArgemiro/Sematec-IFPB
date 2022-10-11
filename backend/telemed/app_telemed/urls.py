from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registrar/medico/', views.registrar_medico, name='registrar_medico')
]