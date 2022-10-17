from django import forms
from .models import Medico, Cliente
from django.contrib import auth
from .encrypting import encriptar_senha

class MedicoFormRegister(forms.Form):
	primeiro_nome = forms.CharField(label='Nome', required=True)
	segundo_nome = forms.CharField(label='Sobrenome', required=True)
	login = forms.CharField(label='Email', required=True)
	senha = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(), strip=False)
	num_pais = forms.CharField(label='Código do país', required=True, max_length = 3)
	num_ddd = forms.CharField(label='DDD', required=True, max_length = 3)
	num_telefone = forms.CharField(label='Telefone', required=True, max_length = 15)
	crm = forms.CharField(label='CRM', required=True, max_length = 15)
	crm_UF = forms.CharField(label='UF', required=True)
	cep = forms.CharField(label='CEP', required=True, max_length = 10)
	endereco = forms.CharField(label='Endereço', required=True, max_length = 50)
	areaAtuacao = forms.CharField(label='Área de Atuação', required=True)

	def save(self):
		data = self.cleaned_data
		senha_enciptada = encriptar_senha(data['senha'])
		medico = Medico(
			username = data['login'],
			first_name = data['primeiro_nome'],
			last_name = data['segundo_nome'],
			password = senha_enciptada,
			num_pais = data['num_pais'],
			num_ddd = data['num_ddd'],
			num_telefone = data['num_telefone'],
			crm = data['crm'],
			crm_UF = data['crm_UF'],
			cep = data['cep'],
			endereco = data['endereco'],
			areaAtuacao = data['areaAtuacao']
		)
		medico.save()

class ClienteFormRegister(forms.Form):
	wdgt = forms.TextInput(attrs={'class':'input-text', 'placeholder':'Digite sua senha...','type':'password'})
	primeiro_nome = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu nome...'}))
	segundo_nome = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu sobrenome...'}))
	login = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu email...'}))
	senha = forms.CharField(label='', required=True, widget=wdgt, strip=False)
	num_pais = forms.CharField(label='', required=True, max_length = 3, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite o código do país...'}))
	num_ddd = forms.CharField(label='', required=True, max_length = 3, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu DDD...'}))
	num_telefone = forms.CharField(label='', required=True, max_length = 15, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu telefone...'}))
	cep = forms.CharField(label='', required=True, max_length = 10, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu CEP...'}))
	endereco = forms.CharField(label='', required=True, max_length = 50, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu endereçoo...'}))

	def save(self):
		data = self.cleaned_data

		senha_enciptada = encriptar_senha(data['senha'])
		cliente = Cliente(
			username = data['login'],
			first_name = data['primeiro_nome'],
			last_name = data['segundo_nome'],
			password = senha_enciptada,
			num_pais = data['num_pais'],
			num_ddd = data['num_ddd'],
			num_telefone = data['num_telefone'],
			cep = data['cep'],
			endereco = data['endereco']
		)
		cliente.save()

class LoginForm(forms.Form):
	username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder':'Digite seu email...'}))
	senha = forms.CharField(label='', strip=False, widget=forms.TextInput(attrs={'placeholder':'Digite sua senha...', 'type':'password'}), required=True)

	def login(self, request):
		data = self.cleaned_data

		if Medico.objects.filter(username=data['username']).exists():
			medico = auth.authenticate(request, username=data['username'], password=data['senha'])
			if medico != None:
				auth.login(request, medico)
				print('Medico Logado')
		elif Cliente.objects.filter(username=data['username']).exists():
			cliente = auth.authenticate(request, username=data['username'], password=data['senha'])
			if cliente != None:
				auth.login(request, cliente)
				print('Cliente Logado')