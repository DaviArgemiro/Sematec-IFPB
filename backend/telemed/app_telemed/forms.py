from django import forms
from .models import Consulta, Medico, Cliente
from django.contrib import auth
from django.contrib.auth.models import User
from .encrypting import encriptar_senha
from .choices import medic_choices

class MedicoFormRegister(forms.Form):
	wdgt = forms.TextInput(attrs={'class':'input-text', 'placeholder':'Digite sua senha...','type':'password'})
	primeiro_nome = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu nome...'}))
	segundo_nome = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu sobrenome...'}))
	login = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu email...'}))
	senha = forms.CharField(label='', required=True, widget=wdgt, strip=False)
	num_pais = forms.CharField(label='', required=True, max_length = 3, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite o código do país...'}))
	num_ddd = forms.CharField(label='', required=True, max_length = 3, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu DDD...'}))
	num_telefone = forms.CharField(label='', required=True, max_length = 15, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu telefone...'}))
	crm = forms.CharField(label='', required=True, max_length = 15, widget=forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Digite seu CRM...'}))
	crm_UF = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Digite o UF do CRM...'}))
	cep = forms.CharField(label='', required=True, max_length = 10, widget=forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Digite seu CEP...'}))
	endereco = forms.CharField(label='', required=True, max_length = 50, widget=forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Digite seu endereço...'}))
	areaAtuacao = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Digite sua área de atuação'}))

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
	endereco = forms.CharField(label='', required=True, max_length = 50, widget=forms.TextInput(attrs={'class':'input-text', 'placeholder': 'Digite seu endereço...'}))

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

class ConsultasForm(forms.Form):

	médico = forms.ChoiceField(choices=medic_choices, required=True)
	status = forms.IntegerField(widget= forms.HiddenInput(), initial=0)
	data_da_consulta = forms.DateTimeField(required=True, widget=forms.TextInput(attrs={'type':'datetime-local'}))
	observação = forms.CharField(max_length= 150, required=True, widget=forms.TextInput(attrs={'class':'input-t'}))



	def save(self, clid):
		data = self.cleaned_data

		consulta = Consulta(
			id_med = data['médico'],
			id_cli = clid,
			data_consulta = data['data_da_consulta'],
			status = data['status'],
			obs = data['observação'],
			link_consulta = None,
			documento = None,
		)
		consulta.save()