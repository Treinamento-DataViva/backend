# Banco de Dados 

O banco de dados do projeto roda em um container Docker utilizando
**PostgreSQL** e **pgAdmin**.

------------------------------------------------------------------------

## Iniciando o ambiente

1.  Acesse a pasta `/db` do projeto:
    cd db

2.  Execute o comando abaixo para iniciar os containers:
    docker compose up -d

Esse comando irá:

-   baixar as imagens necessárias
-   iniciar um container com **PostgreSQL**
-   iniciar um container com **pgAdmin**
-   configurar automaticamente a rede entre os dois serviços

> **Observação:** as variáveis de ambiente estão configuradas apenas
> para desenvolvimento.\
> Atualmente o usuário e senha estão definidos como `admin`.

No caso de erro para subir os containers por conta das portas **5432** ou **5050** já estarem em uso, basta rodar o seguinte comando para liberar as portas:

    sudo kill -9 $(sudo lsof -t -i :5432)
    sudo kill -9 $(sudo lsof -t -i :5050)

------------------------------------------------------------------------

## Acessando o pgAdmin

Após iniciar os containers, o pgAdmin estará disponível em:

    http://localhost:5050

Use as credenciais definidas no arquivo `docker-compose.yml`.

Depois de logar, crie uma conexão com o servidor PostgreSQL utilizando:

    Host: postgres
    Port: 5432
    User: admin
    Password: admin
    Database: censo_escolar

O host `postgres` funciona porque os containers estão conectados pela
mesma rede Docker.

------------------------------------------------------------------------

## Criando o Banco de Dados

Acesse o ambiente do projeto e instale as dependências:

    pip install -r requirements.txt 
    
Acesse o banco de dados do censo escolar no BigQuery e crie um projeto na sua conta.

Com o projeto criado, atualize a variável `censo_escolar` no arquivo `extract.py` com o ID do seu projeto no Google Cloud.

Em seguida, acesse a pasta `scripts` e execute o script de extração para popular o banco de dados:

    python3 etl.py

------------------------------------------------------------------------

## Parando o ambiente

Para parar os containers:

    docker compose down
