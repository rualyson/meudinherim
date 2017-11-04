from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from caixa.forms import LancamentosForm
from caixa.models import LancamentosCaixa, Categoria, SaldoCaixa
from banco.forms import LancamentosBancoForm
from banco.models import LancamentosBanco, ContaBanco
from django.contrib.auth.forms import UserCreationForm
from usuario.forms import UsuarioForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django import forms
from banco.models import ContaBanco, LancamentosBanco
import json


def index(request):
	template = 'principal/index.html'

	if request.method == 'POST':
		form = UsuarioForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(username = user.username, password = form.cleaned_data['password1'])
			login(request, user)
			return redirect('principal:home')
		else:
			form = LoginForm(request.POST)

			if form.is_valid():

				form_login = form.cleaned_data['login']
				form_senha = form.cleaned_data['senha']

				usuario = authenticate(username=form_login,password=form_senha)

				if usuario is not None:
					login(request, usuario)
					return redirect('principal:home')
	form = UsuarioForm()
	form2 = LoginForm()
	context = {'form': form, 'form2':form2}
	return render(request, template, context)

@login_required
def home(request):
	template = 'principal/home.html'
	context = {}
	#id do usuario logado
	id_user = request.user.id

	eventosCaixa = []
	eventosBanco = []

	#carrega os lançamentos do caixa do usuário
	lancamentosCaixa = LancamentosCaixa.objects.filter(user_id = id_user)
	#carrega os lançamentos do banco do usuário
	lancamentosBanco = LancamentosBanco.objects.filter(user_id = id_user)

	#separa os dados do caixa que serão utilizados no calendario em um tupla
	for lancamento in lancamentosCaixa:
		dia = str(lancamento.data.day)
		if(len(dia) == 1):
			dia = "0" + dia
		mes = str(lancamento.data.month)
		if(len(mes) == 1):
			mes = "0" + mes
		ano = str(lancamento.data.year)
		#concatena a data para o formato do fullcalendar
		data = ano + "-" + mes + "-" + dia
		titulo = lancamento.descricao + " : " + " R$" + str(lancamento.valor) 
		eventosCaixa.append((titulo, data))
	
	#converte a tupla para dicionario
	eventosCaixa = [{'title': title, 'start': start} for title, start in eventosCaixa]

	#separa os dados do banco que serão utilizados no calendario em um tupla
	for lancamento in lancamentosBanco:
		dia = str(lancamento.data.day)
		if(len(dia) == 1):
			dia = "0" + dia
		mes = str(lancamento.data.month)
		if(len(mes) == 1):
			mes = "0" + mes
		ano = str(lancamento.data.year)
		#concatena a data para o formato do fullcalendar
		data = ano + "-" + mes + "-" + dia
		titulo = lancamento.descricao + " : " + " R$" + str(lancamento.valor) 
		eventosBanco.append((titulo, data))

	#converte a tupla para para dicionario
	eventosBanco = [{'title': title, 'start': start, 'color': 'yellow', 'textColor': 'black'} for title, start in eventosBanco]
	#junta os lancamento de caixa e banco
	todosEventos = eventosBanco + eventosCaixa
	#converte para o formato Json
	todosEventos = json.dumps(todosEventos, ensure_ascii=False)

	context['events'] = todosEventos
	
	# print(teste)

	formCaixa = LancamentosForm()
	#seleciona apenas as categorias do usuario logado
	formCaixa.fields['categoria'] = forms.ModelChoiceField(
			queryset = Categoria.objects.filter(user_id = request.user.id),
			empty_label = 'Nenhum',
	        widget = forms.Select(
	            attrs = {'class': 'form-control'}
	        )
		)
	
	formBanco = LancamentosBancoForm()
	#Seleciona apenas o banco do usuario para o formulario
	formBanco.fields['banco'] = forms.ModelChoiceField(
		queryset = ContaBanco.objects.filter(user_id = request.user.id),
		empty_label = 'Nenhum',
        widget = forms.Select(
            attrs = {'class': 'form-control'}
        )
	)
	#seleciona apenas as categorias do usuario logado
	formBanco.fields['categoria'] = forms.ModelChoiceField(
			queryset = Categoria.objects.filter(user_id = request.user.id),
			empty_label = 'Nenhum',
	        widget = forms.Select(
	            attrs = {'class': 'form-control', 'id': 'categoria_banco'}
	        )
		)

	#busca o saldo de Caixa do usuario e atribui ao contexto
	saldo = SaldoCaixa.objects.get(user = request.user)
	context['saldoCaixa'] = saldo.saldoAtual

	context['formLancCaixa'] = formCaixa
	context['formLancBanco'] = formBanco

	return render(request, template, context)