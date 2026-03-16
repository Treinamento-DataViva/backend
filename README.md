# backend

## DB - Postgre
 O banco de dados do projeto é executado com postgre rodando em um docker container, para iniciar o banco use 
 'docker compose up -d' para iniciar a imagem e depois
 'docker exec -it censo-escolar-postgres psql -U admin -d censo_escolar' para acessar o banco