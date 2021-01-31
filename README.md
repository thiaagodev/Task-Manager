# Task Manager

Uma API para gerenciamento de tarefas, nela é possível se registrar, logar e criar suas tarefas, também é possível visualizar, editar e excluir tarefas individualmente.

A principal motivação desse repositório é aprender mais sobre o Django rest framework, e também aprender e aplicar conceitos de hash de senha com bcrypt, autenticação com JWT e permissões de usuários.


## O que eu aprendi com esse projeto:

 - Criar sistema de login com autenticação via JWT
 - Armazenamento de senhas com hash bcrypt
 - Permissões de usuários da aplicação
 - Documentação da API com Swagger
 - Criar rotas e views/serializers mais detalhados


### API documentada com Swagger:

<img src='./.github/api_swagger.png' alt='API Swagger'/>


## Como executar o projeto:

    - Para instalar as libs necessárias use o comando "pip3 install -r libs.txt"
    - Ative a venv com "source ./venv/bin/activate"
    - Rode as migrations com "python3 manage.py migrate"
    - Crie um arquivo .env com "JWT_SECRET_KEY=<chave da sua escolha>"
    - Rode o servidor com o comando "python3 manage.py runserver"
