# 🛒 E-commerce em Django

Este é um projeto de **loja virtual** desenvolvido em **Python (Django)**.  
O objetivo é criar um sistema simples de e-commerce com painel administrativo, cadastro de produtos, gerenciamento de usuários e autenticação segura.

## 🚀 Funcionalidades
- Cadastro e login de usuários (com autenticação Django).
- Painel administrativo para gerenciar produtos e perfis.
- Upload e redimensionamento de imagens dos produtos.
- Carrinho de compras básico.
- Validação de dados (como CPF e CEP).
- Integração com Django Debug Toolbar para debug durante o desenvolvimento.

## 🛠️ Tecnologias Utilizadas
- [Python 3.13](https://www.python.org/)
- [Django 4.2+](https://www.djangoproject.com/)
- [SQLite](https://www.sqlite.org/) (banco de dados padrão do Django)
- [Pillow](https://pillow.readthedocs.io/) para manipulação de imagens
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/) para formulários mais elegantes

## 📦 Instalação e Execução

1. Clone este repositório:
   ```bash
   git clone https://github.com/AbelGoncalo/ecomerce-python.git
   cd ecomerce-python
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
http://127.0.0.1:8000/
