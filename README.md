# Desafio Técnico - Sistema de Gestão Escolar 

Este projeto é uma aplicação web fullstack desenvolvida com **Django** e
**Django Rest Framework**, utilizando **PostgreSQL** como banco de dados
e **Docker** para orquestração. O sistema gerencia alunos, cursos,
matrículas e relatórios financeiros.

---

## 🚀 Tecnologias Utilizadas

-   **Linguagem:** Python 3.12\
-   **Framework Web:** Django 5.2.8\
-   **API:** Django Rest Framework (DRF)\
-   **Banco de Dados:** PostgreSQL\
-   **Frontend:** Django Templates + Bootstrap 5\
-   **Infraestrutura:** Docker & Docker Compose

---
## ⚙️ Como Rodar o Projeto (Docker)

Siga os passos abaixo para executar a aplicação em qualquer ambiente:

### 1. Configurar Variáveis de Ambiente

Na raiz do projeto, crie um arquivo `.env` baseado no exemplo fornecido.
Você pode copiar o exemplo:

``` bash
cp .env.example .env
```

Certifique-se de que as credenciais no .env (DB_NAME, DB_USER, etc.)
correspondam ao que você deseja usar.

------------------------------------------------------------------------

### 2. Subir os Containers

Execute o comando abaixo para construir a imagem e iniciar os serviços
(Aplicação + Banco de Dados). O sistema rodará automaticamente as
migrações.

``` bash
docker compose up --build
```

Aguarde até aparecer a mensagem de que o servidor iniciou na porta 8000.

------------------------------------------------------------------------

### 3. Criar um Superusuário (Opcional)

Para acessar o Django Admin ou ter permissão total no sistema, crie um
usuário administrador executando em outro terminal:

``` bash
docker compose exec web python manage.py createsuperuser
```

---

# 🔗 URLs e Acesso

## 🖥️ Frontend

-   Login: http://localhost:8000/
-   Dashboard: http://localhost:8000/dashboard/
-   Alunos: http://localhost:8000/students/
-   Cursos: http://localhost:8000/courses/
-   Financeiro: http://localhost:8000/financci/

## 🔌 API

<sub>Para o gerenciamento através da API, entre como superusuário</sub>

-   API Root: http://localhost:8000/api/
-   Alunos: http://localhost:8000/api/students/
-   Cursos: http://localhost:8000/api/courses/
-   Matrículas: http://localhost:8000/api/registrations/
-   Relatório Financeiro: http://localhost:8000/api/financial-report/

---

# 🛠️ Funcionalidades Específicas do Desafio

### Estatísticas SQL Bruto

http://localhost:8000/api/courses/statistics/

### Matrículas por Aluno

http://localhost:8000/api/students/ID/registrations/

### Marcar como Paga

POST → http://localhost:8000/api/registrations/ID/mark_as_paid/

---

# 📂 Estrutura do Projeto

    core/                  → Configurações do Django
    students/              → App principal
        models.py          → Modelos
        views.py           → Frontend
        api_views.py       → DRF
        serializers.py     → Serialização
        templates/         → HTML/Bootstrap

    desafio_dj.sql         → SQL bruto
    docker-compose.yml     → Serviços Docker
    Dockerfile             → Build

---
