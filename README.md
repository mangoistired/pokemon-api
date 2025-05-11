# 🐱 API de Pokémon

Este projeto é uma API REST feita com Flask que permite montar um time de até 6 Pokémons. Os dados são buscados diretamente da [PokéAPI](https://pokeapi.co/), garantindo informações reais como tipo, imagem e nível inicial.

---

## Funcionalidades

- ✅ **GET** `/time` – Retorna todos os Pokémons do time
- ✅ **POST** `/time` – Adiciona um novo Pokémon (usando nome)
- ✅ **DELETE** `/time/<id>` – Remove um Pokémon do time pelo ID
- ✅ **GET** `/visu` – Página HTML com imagens dos Pokémons 🖼️

---

## Como funciona

- O time é salvo localmente no arquivo `data.json`
- Cada Pokémon é buscado na PokéAPI com nome (ex: "pikachu")
- A resposta inclui nome, tipo, nível e imagem

---

## Como rodar localmente

1. Clone o repositório:
git clone https://github.com/seu-usuario/api-time-pokemon.git
cd api-time-pokemon

Instale as dependências:
    pip install -r requirements.txt

Rode a aplicação:
    python app.py

Acesse no navegador:
    API JSON: http://localhost:5000/time

    Página visual: http://localhost:5000/visu

    Documentação Swagger: http://localhost:5000/apidocs

## Testes com o Postman

A coleção de testes do Postman está disponível no arquivo `postman_collection.json`. Para importar:

1. Abra o Postman.
2. Clique em **Import** no canto superior esquerdo.
3. Selecione o arquivo `postman_collection.json` do repositório.
4. Clique em **Import**.

## Tecnologias usadas
Python + Flask
PokéAPI
HTML + CSS
