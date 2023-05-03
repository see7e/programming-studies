console.log('inicio_jogo')

/* as variaveis precisam ser declaradas antes para que
façam parte do escopo global do script, quando seriam
somente da função se fossem declaradas inicialmente den-
tro dela*/
	var altura_tela = 0 
	var largura_tela = 0 
	var vidas = 3
	var tempo = 10
	var cronometro
	var nivel = window.location.search
	var tempoNivel = 0

/*definição de nível
************************/	
	nivel = nivel.replace('?', '')
	//debug
	console.log(nivel)

	if (nivel==='facil') {
		tempoNivel = 1500
	} else if(nivel==='medio'){
		tempoNivel = 1000
	} else if (nivel==='dificil') {
		tempoNivel = 750
	}
	
/*mudança no tamanho da tela
************************/
	function redimensionarPalco () {
		altura_tela = window.innerHeight
		largura_tela = window.innerWidth
		//debug
		console.log('largura_tela: ', largura_tela, ' / altura_tela: ', altura_tela)
	}

	redimensionarPalco()


/*definição do tempo de jogo
************************/
	var cronometro = setInterval(
		function(){
			tempo -= 1
			//VITÓRIA
			if (tempo<0) {
				//clearInterval para evitar possíveis bugs
				clearInterval(cronometro)		//limpa a contagem de tempo do cronometro
				clearInterval(criarMosquito)		//limpa criação de elementos

				window.location.href = 'vitoria.html'
			} else {
				document.getElementById('tempo').innerHTML = tempo
			}
		}
	, 1000)

/*posições randomicas
************************/
	function posicaoRandom() {

		var posicaoX = Math.floor(Math.random() * largura_tela) - 90
		var posicaoY = Math.floor(Math.random() * altura_tela) - 90

		posicaoX = posicaoX < 0 ? 0 : posicaoX		//operador ternario 
		posicaoY = posicaoY < 0 ? 0 : posicaoY		//(x < 0 ? <se sim> : <se não>)
		//debug
		console.log('x: ', posicaoX, ' / y: ', posicaoY)


		//remover elementos anterior (caso exista)
			if(document.getElementById('mosquito')) {	//basta selecionar o elemento, se ele existir :: vai dar != null, ou seja, true
				document.getElementById('mosquito').remove()

				//DERROTA
				if(vidas==0) {
					window.location.href = 'fim_de_jogo.html'
				} else{
				document.getElementById('v' + vidas).src = "imagens/coracao_vazio.png"
				
				vidas--
				//debug
				console.log('vidas- v' + vidas)
				}
			}

			//SUGESTAO-remover vida junto com o elemento
				
				//se o elemento for removido
				
				//se vidas == 0 :: jogo encerra
		

		//criação dos elementos

			var mosquito = document.createElement('img')
			mosquito.src = 'imagens/mosquito.png'		//modicidação do atributo 'src' do elemento <img>
			mosquito.className = tamanhoRandom() + ' ' + ladoRandom()		//modificação dos tamanhos e lados dos mosquitos

			//movimentaação do elemento
			mosquito.style.position = 'absolute'		//para "desprender" do body
			mosquito.style.left = posicaoX + 'px'
			mosquito.style.top = posicaoY + 'px'

			mosquito.id = 'mosquito'

				//matar o mosquito
				mosquito.onclick = function() {
					this.remove()
				}

			document.body.appendChild(mosquito)			//implandação na API do elemento 'mosquito'
	}

/*veriação de tamanhos
************************/
	function tamanhoRandom () {
		var tamanho = Math.floor(Math.random() * 3)

		//variação das classes
		switch(tamanho) {
			case 0:
				return 'mosquito1'
			case 1:
				return 'mosquito2'
			case 2:
				return 'mosquito3'
		}
	}

	function ladoRandom () {
		var tamanho = Math.floor(Math.random() * 2)

		//variação das classes
		switch(tamanho) {
			case 0:
				return 'ladoA'
			case 1:
				return 'ladoB'
		}
	}