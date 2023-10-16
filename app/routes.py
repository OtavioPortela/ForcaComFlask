from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    nome = 'Otavio Augusto'
    dados = {'profissao': 'Analista de sistemas',
             'idade': 26,
             'tempo': '4 anos'}
    return render_template('index.html', nome='Otavio Augusto', dados = dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')