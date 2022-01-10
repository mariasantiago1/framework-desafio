# Backend

Repositório referente ao Backend do projeto Desafio Teste.

Esse repositório constitui a **API** (_Application Programing Interface_) do sistema, sendo construído:

- Na linguagem de programação **Python**
- Com o _framework_ de desenvolvimento web **FLASK**;

## Configuração Inicial

- Crie um arquivo `.env` na raíz do projeto com as seguintes variáveis semelhantes as do arquivo `.env.sample`:

## Ambiente de Desenvolvimento

1) Certifique-se que o Python instalado em sua máquina seja, no mínimo, a versão 3.7 com `python --version`.
2) Instale o `virtualenv` com o comando `pip install virtualenv` (tutorial: [link](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais)).
3) Acesse a raíz do projeto.
4) Execute o backend com o comando `flask run` (com isso, o servidor de desenvolvimento Flask será executado na porta 5000).

**Obs**: As credenciais de acesso à API consumida já foram geradas pelo script.

## Ambiente Docker

1) Certifique-se que o Docker está instalado.
2) Alterar na variável de ambiente o valor `DB_HOST` para `<nome-container-database>`.
3) Execute na raiz do projeto `docker-compose up --build -d` para subir o projeto.
4) Para criar a estrutura básica do banco execute o comando `docker exec -it <nome-container-database> sh /opt/recria_db_docker.sh`
5) Para importar a massa inicial dos dados execute o comando `docker exec -it <nome-container-django> sh /usr/src/app/scripts/carga.sh`

**Obs**: As credenciais de acesso ao ambiente como superusuário já foi gerado pelo script, no entanto pode ser gerado outro com o comando `docker exec -it <nome-container-django> python manage.py createsuperuser`
## Testes

