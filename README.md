# Sistema de Academia

## Sobre o projeto

O Sistema de Academia é um projeto desenvolvido em Python para simular o gerenciamento de alunos e professores de uma academia.

O projeto começou como uma aplicação executada no terminal, com foco nos fundamentos da Programação Orientada a Objetos (POO), e evoluiu gradualmente para incluir persistência de dados, autenticação de usuários e uma API REST.

O objetivo é aplicar na prática conceitos de desenvolvimento backend, desde a organização do código até a integração com banco de dados e a criação de endpoints protegidos.

## Funcionalidades

- Cadastro, busca, alteração e remoção de alunos e professores;
- Persistência de dados utilizando PostgreSQL;
- Geração automática de IDs pelo banco de dados;
- Validação de nomes, datas de nascimento e IDs;
- Cálculo automático da idade a partir da data de nascimento;
- Tratamento de erros de entrada e exceções;
- Confirmação antes da remoção de registros;
- Autenticação de usuários com login e senha;
- Armazenamento de senhas com hash utilizando bcrypt;
- Autenticação da API por meio de tokens JWT;
- Proteção de rotas que exigem autenticação;
- Documentação interativa da API com Swagger;
- Interface interativa no terminal utilizando Rich.

## Tecnologias utilizadas

- **Python** — linguagem principal;
- **PostgreSQL** — banco de dados relacional;
- **psycopg** — conexão entre Python e PostgreSQL;
- **FastAPI** — desenvolvimento da API REST;
- **Pydantic** — validação dos dados da API;
- **PyJWT** — geração e validação de tokens;
- **bcrypt** — hash de senhas;
- **Rich** — interface no terminal;
- **python-dotenv** — gerenciamento de variáveis de ambiente;
- **Uvicorn** — servidor da API;
- **pwinput** — entrada de senhas no terminal;
- **Git e GitHub** — versionamento do projeto.

## Conceitos aplicados

- Programação Orientada a Objetos (POO);
- Classes, objetos, herança e encapsulamento;
- Propriedades com `@property` e setters;
- Métodos estáticos;
- Validação e normalização de dados;
- Integração entre Python e PostgreSQL;
- Operações CRUD;
- Tratamento de exceções;
- Autenticação e segurança de senhas;
- Autenticação baseada em tokens;
- Separação de responsabilidades em módulos;
- Criação de APIs REST;
- Versionamento com Git e GitHub.

## Como executar o projeto

### Pré-requisitos

- Python instalado;
- PostgreSQL instalado e em execução;
- Git instalado.

### 1. Clone o repositório

```bash
git clone https://github.com/Leonardo-Regato/Sistema-academia.git
cd Sistema-academia
```

### 2. Crie e ative um ambiente virtual

No Windows, utilizando PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Configure o banco de dados

Crie um banco de dados PostgreSQL chamado `sistema_academia`.

Em seguida, execute o conteúdo do arquivo `database/schema.sql` nesse banco para criar as tabelas necessárias.

### 5. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e configure as credenciais de conexão com o PostgreSQL.

Configure também a variável `JWT_SECRET` com uma chave secreta forte e aleatória.

### 6. Crie o primeiro usuário

Execute o script:

```bash
python criar_usuario.py
```

Siga as instruções exibidas no terminal para cadastrar um usuário de acesso.

### 7. Execute a aplicação no terminal

Com o ambiente virtual ativado e na pasta raiz do projeto, execute:

```bash
python __main__.py
```

### 8. Execute a API REST

Para iniciar o servidor de desenvolvimento da API, execute:

```bash
uvicorn api:app --reload
```

A API ficará disponível em:

`http://127.0.0.1:8000`

A documentação interativa dos endpoints pode ser acessada em:

`http://127.0.0.1:8000/docs`

Utilize a documentação para autenticar-se e testar as rotas protegidas da API.

## Objetivo

Mais do que desenvolver um sistema completo, o objetivo deste projeto é aprender na prática como uma aplicação Python evolui, aplicando novos conceitos conforme são estudados e transformando uma aplicação simples em uma estrutura cada vez mais próxima de um sistema real..