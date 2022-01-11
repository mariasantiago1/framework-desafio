# Backend

Repositório referente ao Backend do projeto Desafio Teste.

Esse repositório constitui a **API** (_Application Programing Interface_) do sistema, sendo construído:

- Na linguagem de programação **Python**
- Com o _framework_ de desenvolvimento web **FLASK**;

## Configuração Inicial

- Crie um arquivo `.env` na raíz do projeto com as seguintes variáveis semelhantes as do arquivo `.env.sample`:

## Ambiente de Desenvolvimento

1) Certifique-se que o Python instalado em sua máquina seja, no mínimo, a versão 3.8 com `python --version`.
2) Crie um ambiente virtual e instale as dependencias com o pip.
3) Acesse a raíz do projeto.
4) Execute o backend com o comando `flask run` (com isso, o servidor de desenvolvimento Flask será executado na porta 5000).
5) O projeto possui dois endpoints: `GET / com header Authorization: Bearer $token` e `POST /login com username e password no body em json`.
6) Não é necessário acesso a banco de dados. Usuário e senha foram simplificados sendo fixados no codigo.

**Obs**: As credenciais de acesso à API consumida já foram geradas pelo script.

## Testes
**TO DO**

