$(function() {
	var csrftokenPOST = getCookie('csrftoken');
	//funcao criada para gerar o csrftoken no envio da requisicao POST para o Django
	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie != '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
	}

	$('#form_add_lancamento_caixa').on('submit', function(evento) {
		evento.preventDefault();

		var data = $('#datepickerC').val();
		var categoria = $('#id_categoria').val();
		var descricao = $('#id_descricao').val();
		var valor = $('#id_valor').val();

		var dados = {
			'data': data,
			'categoria': categoria,
			'descricao': descricao,
			'valor': valor,
			'csrfmiddlewaretoken': csrftokenPOST
		}

		$.ajax({
			type: 'POST',
			url: '/caixa/add/',
			data: dados,
			success: function(msg) {
				//mensagem de confirmação
				$.alert({
					title: false,
					content: msg,
					theme: 'material',
					onClose: function() {
						//limpar campos
						$(".modal-body input").val("");
						$("select[name=categoria]").val('')
						
						//recarrega a página
						location.reload();
					}
				});
			},
			error: function(msg) {
				$.alert(msg.responseText);
			},
		});
	});

	$('#form_add_lancamento_banco').on('submit', function(evento) {
		evento.preventDefault();

		var banco = $('#id_banco').val();
		var data = $('#datepickerB').val();
		var tipo = $('#id_tipo').val();
		var categoria = $('#categoria_banco').val();
		var descricao = $('#desc_Banco').val();
		var valor = $('#valor_banco').val();

		var dados = {
			'banco': banco,
			'data': data,
			'tipo': tipo,
			'categoria': categoria,
			'descricao': descricao,
			'valor': valor,
			'csrfmiddlewaretoken': csrftokenPOST
		}

		$.ajax({
			type: 'POST',
			url: '/banco/add/',
			data: dados,
			success: function(msg) {
				$.alert({
					title: false,
					content: msg,
					theme: 'material',
					onClose: function() {
						//limpar campos
						$(".modal-body input").val("");
						$("select[name=categoria]").val('')
						$("select[name=banco]").val('')

						//recarrega a página
						location.reload();
					}
				});
			},
			error: function(msg) {
				$.alert(msg.responseText);
			},
		});
	});
})