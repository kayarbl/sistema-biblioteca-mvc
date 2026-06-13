# 📚 Sistema de Biblioteca - MVC

Sistema desktop para gerenciamento de biblioteca, desenvolvido em Python com PySide6 (interface gráfica) e PostgreSQL (banco de dados), seguindo o padrão de arquitetura MVC (Model-View-Controller).

## ✨ Funcionalidades

- Cadastro e listagem de livros
- Cadastro e listagem de usuários
- Registro de empréstimos e devoluções
- Controle automático da quantidade de exemplares disponíveis

## 🛠️ Tecnologias

- Python 3.x
- PySide6 (Qt para Python)
- PostgreSQL
- psycopg2

## 📁 Estrutura do Projeto

```
Projeto Biblioteca Novo/
├── config/
│   └── conexao.py
├── models/
│   ├── livro_model.py
│   ├── usuario_model.py
│   └── emprestimo_model.py
├── controllers/
│   ├── livro_controller.py
│   ├── usuario_controller.py
│   └── emprestimo_controller.py
├── views/
│   ├── main_window.py
│   ├── livros_view.py
│   ├── usuarios_view.py
│   └── emprestimo_view.py
├── main.py
├── requirements.txt
└── .env.example
```

## ⚙️ Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/kayarbl/sistema-biblioteca-mvc.git
cd sistema-biblioteca-mvc
```

### 2. Crie um ambiente virtual (opcional, recomendado)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Crie um banco PostgreSQL chamado `biblioteca_db` e execute o script SQL abaixo para criar as tabelas:

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    data_cadastro TIMESTAMP DEFAULT NOW()
);

CREATE TABLE livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    ano_publicacao INTEGER,
    quantidade_total INTEGER NOT NULL,
    quantidade_disponivel INTEGER NOT NULL
);

CREATE TABLE emprestimos (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),
    livro_id INTEGER REFERENCES livros(id),
    data_emprestimo DATE NOT NULL,
    data_devolucao_prevista DATE NOT NULL,
    data_devolucao_real DATE,
    status VARCHAR(20) DEFAULT 'EMPRESTADO'
);
```

### 5. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e preencha com suas credenciais do PostgreSQL:

```bash
cp .env.example .env
```

### 6. Execute o programa
```bash
python main.py
```

## 📌 Observações

Projeto desenvolvido para fins de estudo, aplicando o padrão MVC e boas práticas de separação de responsabilidades.