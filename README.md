# Django-Web-And-Rest
# Configurações importantes
## Powershell
OBS: Não se esqueca de configurar o powershell com o comando abaixo (como administrador):
```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```
# Comandos
## Ambiente de desenvolvimento:
Abaixo esta uma lista dos comandos mais utilizados:
1. Criacao do ambiente virtual
	python -m venv venv
2. Ativacao do ambiente virutal
	.venv\Scripts\activate
3. Instalando django
	pip install django
4. Iniciando projeto
	django-admin startproject nome-projeto caminho-projeto
5. Executar servidor 
	python manage.py runserver
## Aula 18.
### Anotações:
django-admin e o manage.py ambos servem para executar os mesmos comandos. Entretanto, o manage.py cria uma variável de ambiente que aponta para um arquivo setting que vem com algumas pré-configurações do projeto e no startprject será feito pelo django-admin, pois o manage.py ainda não foi criado. 

## Aula 19.
### Anotações:
Criado arquivo .json no vscode para facilitar o uso do django. O arquivo irá executar o comando de inicialização do django com o comando: manage.py runserver.

## Aula 20.
### Anotações:
Em urls.py teremos os caminhos de urls do nosso site. Afunção 'path' recebe dois parâmetros( string caminho e uma função de retorno http). 

## Aula 23.
### Anotações:
Criando um app podemos separar as pastas e caminhos de urls de determinada parte do site. Adicionamos as funções no arquivo views.py e os caminhos no urls.py dentro da pasta do app. Já na pasta raiz do django podemos fazer o include do app.urls que puxará as funções deixando o código mais limpo e organizado. 