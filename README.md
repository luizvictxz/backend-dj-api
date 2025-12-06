# Desafio Técnico - Sistema de Gestão Escolar (Estágio Python 2026.1)

Este projeto é uma aplicação web fullstack desenvolvida com **Django** e
**Django Rest Framework**, utilizando **PostgreSQL** como banco de dados
e **Docker** para orquestração. O sistema gerencia alunos, cursos,
matrículas e relatórios financeiros.

------------------------------------------------------------------------

## 🚀 Tecnologias Utilizadas

-   **Linguagem:** Python 3.12
-   **Framework Web:** Django 5.2.8
-   **API:** Django Rest Framework (DRF)
-   **Banco de Dados:** PostgreSQL
-   **Frontend:** Django Templates + Bootstrap 5
-   **Infraestrutura:** Docker & Docker Compose

------------------------------------------------------------------------

## ✨ Funcionalidades

### 1. Funcionalidades Web (Frontend)

-   **Dashboard:** Visão geral com KPIs (Total de Alunos, Cursos Ativos,
    Receita) e últimas matrículas.
-   **Gestão de Alunos:** Listagem, Cadastro, Edição e Exclusão
    (Soft/Hard delete dependendo da regra).
-   **Gestão de Cursos:** CRUD completo com controle de status
    (Ativo/Inativo).
-   **Matrículas:** Associação de alunos a cursos.
-   **Financeiro:** Relatório visual de status de pagamentos
    (Pago/Pendente) e totais devidos.
-   **Autenticação:** Sistema de Login, Registro e Logout.

### 2. API REST (Endpoints)

-   CRUD completo para Alunos, Cursos e Matrículas.
-   Endpoint personalizado para **Marcar Matrícula como Paga**.
-   **Relatório Financeiro JSON:** Total devido por aluno e por curso.
-   **Relatório SQL Bruto:** Estatísticas de alunos por curso usando
    `connection.cursor()` e queries manuais.

------------------------------------------------------------------------

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

------------------------------------------------------------------------

## 🔗 URLs e Acesso

### 🖥️ Frontend (Interface Visual)

-   Login: http://localhost:8000/
-   Dashboard: http://localhost:8000/dashboard/
-   Alunos: http://localhost:8000/students/
-   Cursos: http://localhost:8000/courses/
-   Financeiro: http://localhost:8000/financci/

### 🔌 API Endpoints (DRF)

-   Raiz da API: http://localhost:8000/api/
-   Alunos: http://localhost:8000/api/students/
-   Cursos: http://localhost:8000/api/courses/
-   Matrículas: http://localhost:8000/api/registrations/
-   Relatório Financeiro (JSON):
    http://localhost:8000/api/financial-report/

### 🛠️ Funcionalidades Específicas

1.  URL: http://localhost:8000/api/courses/statistics/

2.  **Listar Matrículas de um Aluno:**\
    URL: http://localhost:8000/api/students/ID_DO_ALUNO/registrations/

3.  **Marcar Matrícula como Paga:**\
    Faça um POST (vazio) para:\
    URL:
    http://localhost:8000/api/registrations/ID_DA_MATRICULA/mark_as_paid/

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

    core/: Configurações globais do Django (settings.py, urls.py).

    students/: Aplicação principal contendo:
        models.py: Definição das tabelas (Student, Course, Registration).
        views.py: Views baseadas em classes e funções para o Frontend.
        api_views.py: ViewSets e APIViews do Django Rest Framework.
        serializers.py: Transformação de dados para JSON.
        templates/: Arquivos HTML com Bootstrap.

    desafio_dj.sql: Arquivo SQL manual solicitado no desafio.
    docker-compose.yml: Orquestração dos containers.
    Dockerfile: Configuração da imagem Python.
