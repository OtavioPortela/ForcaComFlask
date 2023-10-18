from app import app
from flask import render_template
from flask import request
from random import choice, sample
from app import jogo




@app.route('/')
@app.route('/index',  defaults={"nome":"usuario"})
@app.route('/index/<nome>')
def index(nome):
    
    dados = {'profissao': 'Analista de sistemas jr',
             'idade': 26,
             'tempo': '4 anos'}
    return render_template('index.html', nome=nome, dados = dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/forca')
def forca():
    sorteada = jogo.palavraJogo()
    palavra = sorteada[0]
    dica = sorteada[1]
    letras = jogo.letrasForca(palavra)
    espacos = jogo.criarEspacos(letras, palavra)

    return render_template('forca.html', dica = dica, espacos = espacos)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['GET'])
def autenticar():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    return f"Usuario = {usuario} Senha = {senha}"