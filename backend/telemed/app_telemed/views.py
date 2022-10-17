from django.shortcuts import render, redirect
from .forms import MedicoFormRegister, ClienteFormRegister, LoginForm
from .models import Medico, Cliente
from django.contrib.auth import logout

# Create your views here.


def index(request):
	usuario = request.user

	if usuario.is_authenticated:
		if hasattr(usuario, 'medico'):
			medico = Medico.objects.get(id=usuario.id)
			context = {
				'nome': medico.first_name
			}
			return render(request, 'home_medico.html', context)
		elif hasattr(usuario, 'cliente'):
			cliente = Cliente.objects.get(id=usuario.id)
			context = {
				'nome': cliente.first_name
			}
			return render(request, 'home_cliente.html', context)

	return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def login(request):
	formulario = LoginForm(request.POST or None)

	if request.method == 'POST' and formulario.is_valid():
		formulario.login(request)
		return redirect('/')

	context = {
		'form': formulario
	}

	return render(request, 'login.html', context)

def registrar_medico(request):
	formulario = MedicoFormRegister(request.POST or None)

	if request.method == 'POST' and formulario.is_valid():
		formulario.save()
		return redirect('/login/')

	context = {
		'form': formulario
	}

	return render(request, 'registrar_medico.html', context)

def registrar_cliente(request):
	formulario = ClienteFormRegister(request.POST or None)

	if request.method == 'POST' and formulario.is_valid():
		formulario.save()
		return redirect('/')

	context = {
		'form': formulario
	}

	return render(request, 'registrar_cliente.html', context)
