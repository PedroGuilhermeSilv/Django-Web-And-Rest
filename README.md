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
Criado arquivo .jason no vscode para facilitar o uso do django. O arquivo irá executar o comando de inicialização do django com o comando: manage.py runserver.