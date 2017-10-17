from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LancamentosCaixa(models.Model):

	data = models.DateField()
	categoria = models.ForeignKey('Categoria', on_delete = models.CASCADE)
	descricao = models.CharField(max_length = 32)
	valor = models.DecimalField(max_digits = 6, decimal_places = 2)
	user = models.ForeignKey(User, on_delete = models.CASCADE)


	def __str__(self):

		return self.descricao


class Categoria(models.Model):

	descricao = models.CharField(max_length = 32)

	TIPOS = (
		("1", "Entrada"),
		("2", "Saida"),
	)

	tipo = models.CharField(choices = TIPOS, max_length = 2)


	def __str__(self):

		return self.descricao


