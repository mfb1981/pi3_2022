from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
import os, datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort
from sqlalchemy import func
import math

project_dir=os.path.dirname(os.path.abspath(__file__))
database_file="sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app=Flask('__name__')
app.config['SECRET_KEY']='your secret key'
app.config['SQLALCHEMY_DATABASE_URI']=database_file

db=SQLAlchemy(app)

class Posts(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    created=db.Column(db.DateTime, default=datetime.datetime.now)
    #dataP=db.Column(db.String(80), nullable=False)
    os=db.Column(db.String(80), nullable=True)
    nome=db.Column(db.String(80), nullable=False)
    sobrenome=db.Column(db.String(80), nullable=False)
    endereço=db.Column(db.String(80), nullable=False)
    cep=db.Column(db.String(80), nullable=True)
    telefone=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(80), nullable=False)
    placa=db.Column(db.String(80), nullable=False)
    fabricante=db.Column(db.String(80), nullable=False)
    modelo=db.Column(db.String(80), nullable=False)
    serviços=db.Column(db.String(80), nullable=False)
    dataAgend=db.Column(db.String(80), nullable=False)
    horario=db.Column(db.String(80), nullable=False)
    dataEntrada=db.Column(db.String(80), nullable=True)
    dataEntrega=db.Column(db.String(80), nullable=True)
    valorPrevisto=db.Column(db.String(80), nullable=True)
    valorRecebido=db.Column(db.String(80), nullable=True)
    serviçoRealizado=db.Column(db.String(80), nullable=True)
    mensagem=db.Column(db.String(200), nullable=True)
    
def __init__(self, created, title, content):
    self.created=created
    self.title=title
    self.content=content

db.create_all()

@app.route('/')
def inicio():
    return render_template('index_teste.html')

@app.route('/Sobre')
def sobre():
    return render_template('about_teste.html')

@app.route('/Serviços')
def serviços():
    return render_template('post_teste.html')

@app.route('/enviado')
def enviado():
    return render_template('formEnviado_teste.html')

@app.route('/erro_login')
def loginError():
    return render_template('loginError_teste.html')

@app.route('/area_restrita')
def areaRestrita():
        return render_template('restrito_teste.html')

@app.route('/dashboard')
def dashboard():
        return render_template('emConstrução_teste.html')

@app.route('/busca')
def busca():
        return render_template('busca_teste.html')

#@app.route('/busca_nome')
#def buscaNome():
        #return render_template('buscaNome_teste.html')


#@app.route('/login')
#def login():
    #return render_template('login_teste.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    
    if request.method=='POST':
        loginIn=request.form['loginIn']
        senha=request.form['senha']
        if loginIn == "fsgaragem" and senha == "fs123":
            return redirect(url_for('areaRestrita'))
        else:
            return redirect(url_for('loginError'))    
    return render_template('login_teste.html')

#def login():
    #loginIn="fsgaragem"    
    #post=Posts(loginIn=loginIn)
    #db.session.add(post)
    #db.session.commit()            
    #return loginIn

@app.route('/formulario', methods=('GET', 'POST'))
def create():
    
    if request.method=='POST':
        nome=request.form['nome']
        sobrenome=request.form['sobrenome']
        endereço=request.form['endereço']
        cep=request.form['cep']
        telefone=request.form['telefone']
        email=request.form['email']
        placa=request.form['placa']
        fabricante=request.form['fabricante']
        modelo=request.form['modelo']
        serviços=request.form['serviços']
        dataAgend=request.form['dataAgend']
        horario=request.form['horario']
        mensagem=request.form['mensagem']
        
        post=Posts(nome=nome, sobrenome=sobrenome, endereço=endereço, cep=cep, telefone=telefone, email=email, placa=placa, fabricante=fabricante, modelo=modelo, serviços=serviços, dataAgend=dataAgend, horario=horario, mensagem=mensagem)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('enviado'))    
    return render_template('formulario_teste.html')

@app.route('/todosRegistros')
def registros():
    posts = Posts.query.all()
    return render_template('todosRegistros_teste.html', post=posts)

@app.route('/todosRegistros/<string:id>')
def allId(id):
    post=Posts.query.filter_by(id=id).all()
    post2=Posts.query.filter_by(id=id).first_or_404(description='Não encontrado o número de identificação {}'.format(id))
    varN=post2.id
    if varN == id:
        return render_template('individual_teste.html', post=post, id=id)
    else:
        return render_template('individual_teste.html', post=post, id=id)

@app.route('/todosRegistros_restrito')
def registros_restrito():
    posts = Posts.query.all()
    return render_template('todosRegistrosRestrito_teste.html', post=posts)

@app.route('/busca_nome', methods=('GET', 'POST'))
def buscaNome():
    if request.method=='POST':
        nome=request.form['nome']
        return redirect(url_for('funcNomeCliente', nome=nome))
    return render_template('buscaNome_teste.html')

@app.route('/busca_nome/<string:nome>')
def funcNomeCliente(nome):
    post=Posts.query.filter_by(nome=nome).all()
    post2=Posts.query.filter_by(nome=nome).first_or_404(description='Não encontrado o nome do cliente {}'.format(nome))
    varN=post2.nome
    if varN == nome:
        return render_template('buscaNomeResult_teste.html', post=post, nome=nome)
    else:
        return render_template('buscaNomeResult_teste.html', post=post, nome=nome)

@app.route('/busca_id', methods=('GET', 'POST'))
def buscaId():
    if request.method=='POST':
        id=request.form['id']
        return redirect(url_for('funcId', id=id))
    return render_template('buscaId_teste.html')

@app.route('/busca_id/<string:id>')
def funcId(id):
    post=Posts.query.filter_by(id=id).all()
    post2=Posts.query.filter_by(id=id).first_or_404(description='Não encontrado o número de identificação {}'.format(id))
    varN=post2.id
    if varN == id:
        return render_template('buscaIdResult_teste.html', post=post, id=id)
    else:
        return render_template('buscaIdResult_teste.html', post=post, id=id)

@app.route('/busca_entrada', methods=('GET', 'POST'))
def buscaEntrada():
    if request.method=='POST':
        dataEntrada=request.form['dataEntrada']
        return redirect(url_for('funcEntrada', dataEntrada=dataEntrada))
    return render_template('buscaEntrada_teste.html')

@app.route('/busca_entrada/<string:dataEntrada>')
def funcEntrada(dataEntrada):
    post=Posts.query.filter_by(dataEntrada=dataEntrada).all()
    post2=Posts.query.filter_by(dataEntrada=dataEntrada).first_or_404(description='Não foram encontrados dados {}'.format(dataEntrada))
    varN=post2.dataEntrada
    if varN == dataEntrada:
        return render_template('buscaEntradaResult_teste.html', post=post, dataEntrada=dataEntrada)
    else:
        return render_template('buscaIdResult_teste.html', post=post, dataEntrada=dataEntrada)

def get_post(id):
    post=Posts.query.filter_by(id=id).first()
    if post is None:
        abort(484)
    return post

@app.route('/busca_id/<string:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post=get_post(id)

    if request.method=='POST':
        nome=request.form['nome']
        endereço=request.form['endereço']
        cep=request.form['cep']
        telefone=request.form['telefone']
        email=request.form['email']
        placa=request.form['placa']
        fabricante=request.form['fabricante']
        modelo=request.form['modelo']
        serviços=request.form['serviços']
        dataAgend=request.form['dataAgend']
        horario=request.form['horario']
        dataEntrada=request.form['dataEntrada']
        dataEntrega=request.form['dataEntrega']
        valorPrevisto=request.form['valorPrevisto']
        valorRecebido=request.form['valorRecebido']
        serviçoRealizado=request.form['serviçoRealizado']
        #mensagem=request.form['mensagem']
        
        post.nome=nome
        post.endereço=endereço
        post.cep=cep
        post.telefone=telefone
        post.email=email
        post.placa=placa
        post.fabricante=fabricante
        post.modelo=modelo
        post.serviços=serviços
        post.dataAgend=dataAgend
        post.horario=horario
        post.dataEntrada=dataEntrada
        post.dataEntrega=dataEntrega
        post.valorPrevisto=valorPrevisto
        post.valorRecebido=valorRecebido
        post.serviçoRealizado=serviçoRealizado
        #post.mensagem=mensagem
        
        db.session.commit()
        return redirect(url_for('registros_restrito'))

    return render_template('edit_teste.html', post=post)

@app.route('/busca_id/<string:id>/delete', methods=('POST',))
def delete(id):
    post=get_post(id)
    db.session.delete(post)
    db.session.commit()
    flash('"{}" foi apagado com sucesso!'.format(post.id))
    return redirect(url_for('registros_restrito'))



