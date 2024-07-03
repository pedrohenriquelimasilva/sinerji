# Teste Sinerji

<p align="center">
  <a href="#-tecnologias">Especificações e requisitos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-pass">Passo a passo</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-vision">Visão do projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

## 🚀 Especificações e requisitos

Nesse projeto foi usado as seguintes dependencias:

- openai: 0.27.0
- transformers: 4.30.0
- torch: 2.0.1
- argparse: 1.4.0
- TensoFlow: 2.16
- Python: 3.12

Alerto que o python é necessario está acima do 3.7 para funcionar perfeitamente a aplicação

## 💻 Projeto

Projeto desenvolvido em vistude do teste de competencia disponibilizado pela Sinerji, empresa que realiza gestão e controle de dados, soluções digitais e de software. Neste projeto foi utilizado diversos padrões de design patterns como: Strategy para escolha eficiente de uma avaliação, Observer para notificação do úsuario, Command para gerar os comandos via terminal e Factory para integração aos modelos LLM.

## Passo a passo

1. Fazer clonagem do repositorio ou baixar em sua máquina

2. Gerar uma chave secreta na OpenAI para o vinculo com a aplicação

3. Inserir chave secreta em um arquivo .env com o nome: OPENAI_API_KEY

4. Instalar todas as dependencias com o comando no terminal: pip install

5. Chamada base do modelo: python app.py --model chatgpt --question "Olá, Modelo! Quanto vale 4 x 4?" --eval_strategy length

6. Para selecionar o modelo, utilizaremos --model chatgpt ou --model bert

7. Para informar a pergunta ao modelo, utilizaremos --question 'pergunta'

8. Para definir qual a estrategia de avaliação a ser usada, utilizaremos --eval_strategy length ou keyword

9. Especificamos a keyword com --keyword (palavra-chave)

# Visão do projeto

[![Alt Text](https://img.youtube.com/vi/RXwE4Q9KTkA/0.jpg)](https://www.youtube.com/watch?v=RXwE4Q9KTkA)

<br>
<br>
<br>
<br>
<br>
<br>

<p align="center">Made by Pedro Henrique Lima</p>
