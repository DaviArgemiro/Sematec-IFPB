from pydoc import cli
from django.shortcuts import render, redirect
from .forms import MedicoFormRegister, ClienteFormRegister, LoginForm, ConsultasForm
from .models import Medico, Cliente, Consulta
from django.contrib.auth import logout

# Create your views here.


def index(request):
	usuario = request.user

	if usuario.is_authenticated:
		if hasattr(usuario, 'medico'):
			consultas2 = Consulta.objects.filter(id_med=usuario.id)
			medico = Medico.objects.get(id=usuario.id)
			if consultas2 != None:
				context = {
					'nome': f'{medico.first_name}  {medico.last_name}',
					'consultas': consultas2,
					'telefone': f'{medico.num_pais} ({medico.num_ddd}) {medico.num_telefone}',
					'cep': medico.cep,
					'endereco': medico.endereco
				}
			else:
				context = {
					'nome': f'{medico.first_name}  {medico.last_name}',
					'telefone': f'{medico.num_pais} ({medico.num_ddd}) {medico.num_telefone}',
					'cep': medico.cep,
					'endereco': medico.endereco
				}
			return render(request, 'home_medico.html', context)
		elif hasattr(usuario, 'cliente'):
			consultas = Consulta.objects.filter(id_cli=usuario.id)
			cliente = Cliente.objects.get(id=usuario.id)
			if consultas != None:
				context = {
					'nome': f'{cliente.first_name}  {cliente.last_name}',
					'consultas': consultas,
					'telefone': f'{cliente.num_pais} ({cliente.num_ddd}) {cliente.num_telefone}',
					'cep': cliente.cep,
					'endereco': cliente.endereco
				}
			else:
				context = {
					'nome': f'{cliente.first_name}  {cliente.last_name}',
					'telefone': f'{cliente.num_pais} ({cliente.num_ddd}) {cliente.num_telefone}',
					'cep': cliente.cep,
					'endereco': cliente.endereco
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
		return redirect('/login/')

	context = {
		'form': formulario
	}

	return render(request, 'registrar_cliente.html', context)

def registrar_consulta(request):
	cliente = request.user

	formulario = ConsultasForm(request.POST or None)

	if request.method == 'POST' and formulario.is_valid():
		formulario.save(clid=cliente.id)
		return redirect('/')

	context = {
		'form': formulario,
	}

	return render(request, 'registrar_consulta.html', context)

def aceitar_consulta(request, consulta_id):
	medico = request.user

	if medico.is_authenticated and hasattr(medico, 'medico'):
		consulta = Consulta.objects.get(id=consulta_id)
		if consulta.id_med == medico.id:
			consulta.status = 1
			consulta.save(update_fields=['status'])
		else:
			return redirect('/')
	return redirect('/')

def negar_consulta(request, consulta_id):
	medico = request.user

	if medico.is_authenticated and hasattr(medico, 'medico'):
		consulta = Consulta.objects.get(id=consulta_id)
		if consulta.id_med == medico.id:
			consulta.status = 2
			consulta.save(update_fields=['status'])
		else:
			return redirect('/')
	return redirect('/')

