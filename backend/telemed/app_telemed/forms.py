from django import forms
from .models import Medico, Cliente
from django.contrib import auth
from .encrypting import encriptar_senha

class MedicoFormRegister(forms.Form):
	primeiro_nome = forms.CharField(label='Nome', required=True)
	segundo_nome = forms.CharField(label='Sobrenome', required=True)
	login = forms.CharField(label='Email', required=True)
	senha = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(), strip=False)
	num_pais = forms.CharField(label='Código do país', required=True)
	num_ddd = forms.CharField(label='DDD', required=True)
	num_telefone = forms.CharField(label='Telefone', required=True)
	crm = forms.CharField(label='CRM', required=True)
	crm_UF = forms.CharField(label='UF', required=True)
	cep = forms.CharField(label='CEP', required=True)
	endereco = forms.CharField(label='Endereço', required=True)
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
	primeiro_nome = forms.CharField(label='Nome', required=True)
	segundo_nome = forms.CharField(label='Sobrenome', required=True)
	login = forms.CharField(label='Email', required=True)
	senha = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(), strip=False)
	num_pais = forms.CharField(label='Código do país', required=True)
	num_ddd = forms.CharField(label='DDD', required=True)
	num_telefone = forms.CharField(label='Telefone', required=True)
	cep = forms.CharField(label='CEP', required=True)
	endereco = forms.CharField(label='Endereço', required=True)

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