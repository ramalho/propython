# coding: utf-8

import os
from random import shuffle

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

class Grupo(db.Model):
    administrador = db.UserProperty(required=True)
    nome = db.StringProperty(verbose_name=u'Nome do grupo', required=True)
    criacao = db.DateTimeProperty(auto_now_add=True)
    
    def qt_participantes(self):
        return self.participante_set.count()    

class Participante(db.Model):
    email = db.EmailProperty(required=True)
    grupo = db.ReferenceProperty(Grupo, required=True)
    usuario = db.UserProperty() # login do participante no Google
    beneficiario = db.SelfReferenceProperty()
    # o nome-código é usado nas mensagens para não identificar o remetente
    nome_codigo = db.StringProperty(verbose_name=u'Nome código')
    # o beneficiario é a pessoa que o participante vai presentear
    ultima_visita = db.DateTimeProperty()
    
    def ativo(self):
        return bool(self.usuario and self.nome_codigo and self.beneficiario)
    
    def marca(self):
        if self.ativo():
            return u'\u2714' # ✔
        else:
            return u'\u2718' # ✘
        
    def __str__(self):
        return self.email
  
class Mensagem(db.Model):
    remetente = db.UserProperty(required=True)
    destinatario = db.UserProperty() # se None, a mensagem será para todos
    resposta_de = db.SelfReferenceProperty()
    texto = db.TextProperty(required=True)
    criacao = db.DateTimeProperty(auto_now_add=True)
  
class Home(webapp.RequestHandler):
    def get(self):
        participacoes = []
        usr = users.get_current_user()
        if usr:
            logado = True
            link_logout = users.create_logout_url('/')
            consulta = Grupo.all().filter('administrador = ',
                                             users.get_current_user())
            grupos_administra = consulta.fetch(100)
        else:
            logado = False
            link_login = users.create_login_url(self.request.uri)    
        html = os.path.join(TEMPLATE_DIR, 'index.django.html')
        self.response.out.write(template.render(html, locals()))

class PaginaFechada(webapp.RequestHandler):
    def autenticar(self):
        self.usr = users.get_current_user()
        if not self.usr:
            self.redirect(users.create_login_url(self.request.uri))
        return self.usr
    def devolver(self, html, **vars):
        vars['link_logout'] = users.create_logout_url('/')
        html = os.path.join(TEMPLATE_DIR, html)
        self.response.out.write(template.render(html, locals()))
    def get(self):
        if not self.autenticar(): return
        self.devolver(self.get_pagina)       
        
class CriarGrupo(PaginaFechada):
    html = os.path.join(TEMPLATE_DIR, 'editar_grupo.django.html')
    def get(self):
        self.response.out.write(template.render(self.html, {}))
    def post(self):
        if not self.autenticar(): return
        nome = self.request.get('nome')
        grupo = Grupo(administrador=users.get_current_user(), nome=nome)
        grupo.put()
        emails = self.request.get('emails').split()
        shuffle(emails)
        primeiro = ultimo = Participante(email=emails[-1], grupo=grupo)
        primeiro.put()
        for email in emails[:-1]:
            participante = Participante(email=email, grupo=grupo, beneficiario=ultimo)
            participante.put()
            ultimo = participante
        primeiro.beneficiario = ultimo
        primeiro.put()
        self.redirect('/')
        
class ListarGrupo(PaginaFechada):
    html = os.path.join(TEMPLATE_DIR, 'listar_grupo.django.html')
    def get(self):
        chave = self.request.get('key')
        grupo = db.get(chave)
        nome = grupo.nome
        participantes = grupo.participante_set.order('email')
        self.response.out.write(template.render(self.html, locals()))    

application = webapp.WSGIApplication(
        [
            ('/', Home),
            ('/criar', CriarGrupo),
            ('/grupo', ListarGrupo),
        ],
        debug=True
    )

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
  
  
NOMES = '''
    Carlos
    Joao
    Gloria
    Kelly
    Bia
    Diana
    Lara
    Flora
    Elias
    Ines
    Heitor
    Alberto
'''
