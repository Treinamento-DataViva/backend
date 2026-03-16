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

## Parando o ambiente

Para parar os containers:

    docker compose down
