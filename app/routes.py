from app import app
from flask import render_template, request, jsonify

from random import choice, sample
from app import jogo


#variavel para armazenar o valor do input
letra = None

@app.route('/detalhes')
def index():   
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/' )
def forca():
    sorteada = jogo.palavraJogo()
    palavra = sorteada[0]
    dica = sorteada[1]
    letras = jogo.letrasForca(palavra)
    espacos = jogo.criarEspacos(letras, palavra)
    

    return render_template('forca.html', dica = dica, espacos = espacos)

@app.route('/atualizar_letra', methods = ['POST'])
def pegar():
    global letra
    letra = request.form.get('letra')
    
    return jsonify({'status': 'ok'})
