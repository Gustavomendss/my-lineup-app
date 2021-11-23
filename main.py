# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# instalar o django (terminal console)
pip install django

#Iniciando o projeto DJANGO (terminal console)
 django-admin startproject LINEUP .

#Criando a aplicacao DJANGO (terminal console)
 django-admin startapp LINEUPAPP

''' 

CONFIGURACAO DO SETTING.PY
Passo 1 : IR ATE O CAMINHO C:\Users\GUSTAVO\PycharmProjects\LINEUP\LINEUP\settings.py 
Passo 2 : MODIFICAR O  'INSTALLED_APPS E ADICIONAR  O TEXTO 'LINEUPAPP'
Passo 3 : ALTERAR SECCAO  LANGUADE_CODE PARA 'pt-br' e TIME_ZONE PARA 'AMERICA/Sao_paulo
Passo 4 : INSERIR NO FIM DA PAGINA : 
            STATIC_root = os.path.j
            oin(BASE_DIR , 'staticfiles')
            MEDIA_URL = 'media/'
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
Passo 5 : FECHAR ARQUIVO SETTINGS.PY 

CONFIGURACAO DO MODELS.PY
Passo 1 : IR ATE O CAMINHO C:\Users\GUSTAVO\PycharmProjects\LINEUP\LINEUPAPP\models.py
Passo 2 : CRIAR CLASSES ABSTRATAS  - class Base
from django.db import models

# CRIANDO O  MODELO PARA O LINEUP
class Base(models.Model):
    criacao = models.DateTimeField(auto_created=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Lineupapp(Base):
    título = models.CharField(max_length=255)
    url = models.URLField(unique=True)


    class Meta:
        verbose_name = LineUP
        verbose_name = LineUP


    def __str__(self):
        return self.título

# Criando a parte de avaliacao
class Avaliacao(Base):
    lineup = models.ForeignKey(Lineupapp,
                               related_name='avaliacoes',
                               on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

        class Meta:
            verborse_name = 'Avaliação'
            verborse_name_plural = 'Avaliações'
            unique_together = ['email','lineup']


            def __str__(self):
                return f'{self.nome} avaliou o lineup {self.lineup} com a nota {self.avaliacao}'


CONFIGURACAO DO admin.PY

Passo 1 : ir ate o arquivo 'C:\\Users\\GUSTAVO\\PycharmProjects\\LINEUP\\LINEUPAPP\\admin.py'
from django.contrib import admin
from .models import Lineupapp, Avaliacao

@admin.register(Lineupapp)
class LineupAdmin(admin.ModelAdmin):
    list_display = ('título','url', 'criacao', 'atualizacao','ativo')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('lineup','nome', 'email', 'avaliacao', 'criacao', 'atualizacao', 'ativo')
    


     
 E MODIFICAR O 'INSTALLED_APPS E ADICIONAR  O TEXTO LINEUPAPP


# CRIANDO UM ARQUIVO PARA GRAVAR AS ALTERACOES
PASSO 1 : ABRIR TERMINAL E DIGITAR python manage.py makemigrations 
PASSO 2 : EXECUTAR A MIGRACAO DOS ARQUIVOS:

       python manage.py migrate
PASSO 3 : CRIAR UM SUPER USUARIO
       python manage.py createsuperuser
       endereco de email sera : admin@admin.com
       password : univesp_teste


# APOS AS CONFIGURACOES INICIAR O SERVER
        python manage.py runserver

#PASSO 4 
#Criando o controle de versão para o projeto
git init
git config --global user.name "gustavomendss"
git config --global user.email gustavomendes95.gm@gmail.com

criar o arquivo .gitignore para ignorar arquivos desnecessários e colar :
*.pyc
*~
__pycache__
myvenv
db.sqlite3
/static
.DS_Store



# verificar as mudanças com git status

# salvar as alterações com :
git add -all
git commit -m "My LineUp app, first commit"


# entrar no github e criar um repositorio do zero

apos criação 

git remote add origin https://github.com/Gustavomendss/my-lineup-app.git
git branch -M main
git push -u origin main




Entrar no site PythonAnywhere e criar uma conta
Apos criar iniciar console e digitar o seguinte comando >

pip install --user pythonanywhere
git remote add orign  https://github.com/Gustavomendss/my-lineup-app.git  







'''




# criando o arquivo de configurações
#manage.py startapp lineup
