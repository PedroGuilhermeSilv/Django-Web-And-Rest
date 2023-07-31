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

# Seção 5 Django Urls, Views e templates:	
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


## Aula 24.
### Anotações:
Quando criar um app o django deve ser informado, indo em settings.py em INSTALLED_APPS. Problema de colisão de nomes ocorre quando temos dois arquivos com nomes iguais, o django irá retornar o primeiro que encontrar. Para solucionar é bom usar name espace, ou seja, alterne os nomes dos arquivos ou adicione em uma subpasta para diferenciar.

## Aula 28.
### Anotações:
O Django trabalha com separação das páginas. Por exemplo, nosso app Recipe terá "pages" e "partials" onde o primeiro terá as páginas e o segundo as partes que se irão ser repetidas nas demais páginas. Além disso, para execução de um comando no código html o Django usa a tag {% comando %}.

# Seção 6: Django Staticfiles: Arquivos estáticos (imagens, css, javascript, etc)
## Aula 37 a 41
### Anotações:
O Django organiza os arquivos estáticos (e.g. images, JavaScript, CSS) para serem carregados de uma pasta especificas. A pasta com nome "static" será busca no seu app, mas sempre use o nameespace para diferenciar cada tipo de arquivo e não gerar conflitos. Para saber mais use a documentação:  
https://docs.djangoproject.com/en/4.2/howto/static-files/

# Seção 7: Django Templates: herança, blocos, if, for e mais: 
## Aula 42
### Anotações:
É possível passar parâmetros pela urls através do path em urls.py. 
Leia: https://docs.djangoproject.com/pt-br/3.2/topics/http/urls/ 

## Aula 44 e 45
### Anotações:
É possível herdar de uma página html geral por exemplo: A maioria dos sites em suas páginas possuem o mesmo header e footer. Em sua página base use {% block name %}{% endblock name %} para identificar onde será o local que você insirar novos containers. Já na sua nova página você {% extends 'global/base.html' %} e usa o mesmo comando inicial de block para inserir os novos dados. Mas, lembre-se de informar para o django em settings.py-TEMPLATES-DIRS o caminho da pasta onde está o arquivo base.

## Aula 46
### Anotações:
Podemos automatizar o preechimento temporário do nosso site. Criando um arquivo factory.py e usando a biblioteca Faker é possível gerar dados aletórios e inserir no HTML. Primeiro vá em views.py e importe seu código (from utils.recipe.factory import make_recipe), abra o campo context{} para retornar a variável para o HTML 
```
def recipe(request,id):
    return render(request,'recipe/pages/recipe-view.html',context={
    'recipe':make_recipe(),'is_details_page':True,
    })
```
Indo para seu código HTML agora podemos importar as funções de acordo com o nome da variável que foi passada:
``` 
 <div class="recipe-meta-text">
    {{recipe.servings}} Porções 
 </div>
 ```

## Aula 49
### Anotações:
É possível também fazer Namespace das urls. Criar uma variável em urls.py chamada app_name= 'recipe'.
No path adicione a vairável: name="home".
Em seu código html você pode usar o {% url 'recipes:home' %} no local do link. 
Isso fará com que o site se torne mais dinâmico.

# Seção 8: Django Models e ORM (Object Relational Mapper)

## Aula 51
### Anotações:
Em Django, "models" se refere à parte do framework que lida com a definição e interação com o banco de dados. Os models são classes Python que representam tabelas no banco de dados e definem os campos e comportamentos dessas tabelas. Eles são fundamentais para a criação e manipulação dos dados em um aplicativo Django.

## Aula 52
### Anotações:
Em Django, as "migrations" são um mecanismo que permite gerenciar e aplicar as alterações no esquema do banco de dados de forma automatizada, permitindo que você defina a estrutura do banco de dados usando classes Python (models) e, em seguida, sincronize automaticamente essa estrutura com o banco de dados real.

## Aula 54
### Anotações: 
Podemos usar o django admin para fazer uso dos nosso models cadastrados. Em admin.py você criará uma classe admin para seu models, importar o model e adicionará ele com a função:
```
admin.site.register(Model,ModelAdmin)
```
 ou 
 ```
 com @admin.register(Recipe).
 ```

## Aula 56. (Conhecendo o Django Shell e manipulando QuerySets com ele)
No Django, o shell é uma ferramenta útil que permite interagir com sua aplicação web através da linha de comando. Ele é especialmente útil para depurar, testar e explorar os dados do banco de dados e a lógica de sua aplicação. Para acessar o shell do Django, você pode usar o comando python manage.py shell no diretório raiz do seu projeto.
link da documentação: https://docs.djangoproject.com/pt-br/3.2/ref/models/querysets/ 
