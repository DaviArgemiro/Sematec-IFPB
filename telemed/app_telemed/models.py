from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Medico(User):
	num_pais = models.CharField(max_length = 3)
	num_ddd = models.CharField(max_length = 3)
	num_telefone = models.CharField(max_length = 15)
	crm = models.CharField(max_length = 15)
	crm_UF = models.CharField(max_length = 2)
	cep = models.CharField(max_length = 10)
	endereco = models.CharField(max_length = 50)
	areaAtuacao = models.CharField(max_length = 50)

class Cliente(User):
	num_pais = models.CharField(max_length = 3)
	num_ddd = models.CharField(max_length = 3)
	num_telefone = models.CharField(max_length = 15)
	cep = models.CharField(max_length = 10)
	endereco = models.CharField(max_length = 50)

class Consulta(models.Model):
	id_med = models.BigIntegerField()
	id_cli = models.BigIntegerField()
	data_requisito = models.DateTimeField(auto_now_add = True, editable=False)
	data_consulta = models.DateTimeField()
	obs = models.CharField(max_length = 150)
	link_consulta = models.URLField(null = True, blank = True)
	status = models.IntegerField()
	documento = models.ImageField(null = True, blank = True)
	
