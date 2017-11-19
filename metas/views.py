from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from banco.models import ContaBanco, LancamentosBanco, SaldoBanco
from caixa.models import Categoria, SaldoCaixa
from banco.forms import ContaBancoForm, LancamentosBancoForm
from caixa.forms import LancamentosForm
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from metas.forms import MetasForm
from metas.models import Metas
from usuario.models import UsuarioProfile
import json

@login_required
def metas(request):
	if(request.method == 'POST'):
		form = MetasForm(request.POST)

		if(form.is_valid()):
			cadastroMeta=form.save(commit = False)
			cadastroMeta.user=request.user
			cadastroMeta.progresso = 0
			cadastroMeta.save()
			return HttpResponseRedirect('/metas/')	

	user = request.user
	template='meta/metas.html'
	contexto = {}

	metas = Metas.objects.filter(user = user)
	contexto['formMetas'] = metas

	#busca o saldo de Caixa do usuario e atribui ao contexto
	saldoC = SaldoCaixa.objects.get(user = request.user)
	contexto['saldoCaixa'] = saldoC.saldoAtual

	#busca o saldo de Banco do usuario e atribui ao contexto
	saldoB = SaldoBanco.objects.get(user = request.user)
	contexto['saldoBanco'] = saldoB.saldoAtual

	for m in metas:
		progresso = ((saldoB.saldoAtual + saldoC.saldoAtual) / m.valor) * 100
		m.progresso = round(progresso, 2)
		m.save()

	form = MetasForm() 	

	contexto['formCad'] = form

	userProfile = UsuarioProfile.objects.get(user = request.user)
	contexto['profile'] = userProfile

	return render(request, template, contexto)

@login_required
def editMeta(request):
	user = request.user

	if(request.method == 'POST'):

		#id da meta clicada
		idMeta = request.POST.get('id')
		#busca a meta a ser alterado
		meta = Metas.objects.get(pk = idMeta)
		
		#atribui a meta ao form	
		form = MetasForm(request.POST, instance = meta)

		if(form.is_valid()):
			form.save()

			return HttpResponse('Meta alterada com sucesso')
		else:
			return HttpResponseBadRequest('Dados inválidos. Tente novamente')

	idMeta = request.GET.get('id')

	#busca a meta no banco
	meta = Metas.objects.get(pk = idMeta)

	form = MetasForm(instance = meta)

	form.fields['dataInicio'] = forms.DateField(
		label = 'Data Inicio',
		required = True,
		widget = forms.TextInput(
			attrs = {'class': 'form-control', 'id': 'datepickerMI-alter_meta', 'placeholder': 'Insira a início da meta'}
        )
    )

	form.fields['dataFim'] = forms.DateField(
		label = 'Data Fim',
        required = True,
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'id': 'datepickerMF-alter_meta', 'placeholder': 'Insira a fim da meta'}
            )
        )

	form.fields['titulo'] = forms.CharField(
        label = 'Título da Meta',
        max_length = 40,
        required = True,
        widget = forms.TextInput(
        attrs = {'class': 'form-control', 'id': 'id_titulo-alter_meta', 'placeholder': 'Insira o título da meta'}
        )
    )

	form.fields['valor'] = forms.DecimalField(
        label = 'Valor da Meta',
        min_value = 1,
        max_value = 999999.99,
        required = True,
        widget = forms.NumberInput(
        attrs = {'class': 'form-control', 'id': 'id_valor-alter_meta', 'placeholder': 'Insira o valor da meta'}
        )
    )

	#retorna o id da meta junto com o formulario
	divId = "<div id='id_meta'>" + idMeta + "</div>"

	form_html = {form.as_p(), divId}

	return HttpResponse(form_html)

@login_required
def delMeta(request):
	if(request.method == 'POST'):
		#id do usuario
		user = request
		#id da meta a ser deletada
		idMeta = request.POST.get('id')

		#busca o lançamento
		meta = Metas.objects.get(pk = idMeta)		
		print(meta)
		if(request.user == meta.user):
			meta.delete()

			return HttpResponse("Meta excluída com sucesso")
		else:
			return HttpResponse("Meta não encontrada.")
		

	return HttpResponse("Meta não encontrada.")
