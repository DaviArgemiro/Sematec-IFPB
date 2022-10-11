from django.shortcuts import render, redirect
from .forms import MedicoFormRegister, ClienteFormRegister

# Create your views here.


def index(request):
	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')

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
