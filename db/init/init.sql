CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE escola (
    id SERIAL PRIMARY KEY,
    id_escola INTEGER UNIQUE,

    ano INTEGER,
    nome_escola TEXT,
    sigla_uf TEXT,
    rede TEXT,

    agua_potavel BOOLEAN,
    agua_inexistente BOOLEAN,
    energia_inexistente BOOLEAN,
    esgoto_inexistente BOOLEAN,
    tratamento_lixo_inexistente BOOLEAN,
    banheiro BOOLEAN,
    biblioteca BOOLEAN,
    cozinha BOOLEAN,
    dormitorio_aluno BOOLEAN,
    laboratorio_informatica BOOLEAN,
    laboratorio_ciencias BOOLEAN,
    quadra_esportes BOOLEAN,
    refeitorio BOOLEAN,
    alimentacao BOOLEAN
);

CREATE TABLE localizacao (
    id SERIAL PRIMARY KEY,
    id_escola INTEGER UNIQUE,

    nome TEXT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,

    FOREIGN KEY (id_escola) REFERENCES escola(id_escola)
);
