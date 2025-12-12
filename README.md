# Desafio Técnico - Sistema de Gestão Escolar (Estágio Python 2026.1)

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

# ⚙️ Como Rodar o Projeto --- Passo a Passo

Abaixo está o processo completo, desde a criação do ambiente virtual até
a execução com Docker.

---

## ✅ 1. Criar e Ativar o Ambiente Virtual

Se quiser rodar o projeto localmente:

```bash
python -m venv venv
```

Ativar o ambiente:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## ✅ 2. Instalar as Dependências (Modo Local)

```bash
pip install -r requirements.txt
```

---

## ✅ 3. Configurar Variáveis de Ambiente

Crie o arquivo `.env`:

```bash
cp .env.example .env
```

Edite conforme necessário (DB_NAME, DB_USER etc.).

---

# 🚢 4. Executar com Docker (Recomendado)

### Iniciar containers:

```bash
docker compose up --build
```

O servidor iniciará automaticamente após as migrações.

---

## 👤 5. Criar Superusuário

```bash
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

# 👤 Autor

Projeto desenvolvido como parte do processo seletivo para Estágio
Python/Django 2026.1.
