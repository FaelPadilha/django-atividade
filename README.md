# Atividade de Django e React (Desenvolvimento de Sistemas Web)

## 🔧 Bibliotecas Utilizadas no Ambiente Virtual (Django)
- Django (pip install django)
- Django Rest Framework (pip install djangorestframework)
- Django CORS Headers (pip install django-cors-headers)
- Rest Framework Simple JWT (pip install djangorestframework-simplejwt)

## 🔧 Observações (Banco de dados)
O projeto está utilizando a biblioteca Psycopg2 para se conectar com o Banco de dados PostgreSQL:
- Psycopg2 (pip install psycopg2-binary)

Altere para o MySQL instalando a seguinte biblioteca:
- MySQL Client (pip install mysqlclient)

Além disso, altere a conexão no arquivo settings.py no diretório banco/.

```sql
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

No arquivo settings.py o CORS está configurado para receber requisições de qualquer porta.

```python
CORS_ALLOW_ALL_ORIGINS = True
```

No arquivo settings.py a API não está renderizando em JSON. Para alterar isso basta entrar no arquivo settings.py e descomentar o seguinte código:

```python
REST_FRAMEWORK = {
    #'DEFAULT_RENDERER_CLASSES': [
    #    'rest_framework.renderers.JSONRenderer',
    #],
    ...
} 
```

Para instalar o node_modules basta entrar no diretorio frontend/ e executar o seguinte comando:

```js
npm install
```
