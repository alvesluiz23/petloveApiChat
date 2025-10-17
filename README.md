
# 🐶🐈 Chat Petlove

## 🚀 Sobre o projeto
  Esse projeto é um chatbot para atendimento de clientes interessados nos produtos da petlove

## 🖥️  Tecnologias utilizadas
  - Python 
  - Flask
  - Germini api
  - Docker
  
## Como executar o projeto

 - Clone o repositorio localmente
 - No diretorio raiz, crie um arquivo chamado .env e adicione o conteúdo  "api_germini_key=(colocar sua chave do germini api aqui)"
 - Execute o comando **docker build --tag chatbot .** para buildar a imagem
 - Em seguida, **docker run --network=host chatbot** para executar o projeto

O projeto já estará disponivel, bastando apenas fazer as requisições http no local indicado após a execução do comando de run

Exemplo de comando curl:

curl --location 'http://127.0.0.1:5000/api/question-and-answer' \
--header 'Content-Type: application/json' \
--data  '{"question": "Melhor ração para um caramelo"}'
