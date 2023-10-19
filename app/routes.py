from app import app
from flask import render_template
from flask import request
from random import choice, sample
from app import jogo


#variavel para armazenar o valor do input
letra_recebida = None

@app.route('/detalhes')
def index():   
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/')
def forca():
    sorteada = jogo.palavraJogo()
    palavra = sorteada[0]
    dica = sorteada[1]
    letras = jogo.letrasForca(palavra)
    espacos = jogo.criarEspacos(letras, palavra)

    return render_template('forca.html', dica = dica, espacos = espacos)

