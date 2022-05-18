# Atividade de Django e React (Desenvolvimento de Sistemas Web)

## 🔧 Bibliotecas Utilizadas no Ambiente Virtual (Django)
- Django (pip install django)
- Django Rest Framework (pip install djangorestframework)

## 🔧 Observações (Banco de dados)
O projeto está utilizando a biblioteca Psycopg2 para se conectar com o Banco de dados PostgreSQL:
- Psycopg2 (pip install psycopg2-binary)

Altere para o MySQL instalando a seguinte biblioteca:
- MySQL Client (pip install mysqlclient)

Além disso, altere a conexão no arquivo settings.py no diretório banco/.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'NOME DO BANCO DE DADOS',
        'USER': 'root',
        'PASSWORD': 'PASSWORD',
        'HOST': '127.0.0.1',
        'PORT': '3306',  
    }
}
```

