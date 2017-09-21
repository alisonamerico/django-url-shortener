# Grow
A simple URL shortener developed in Django

![Alt Text](https://github.com/alisonamerico/django-url-shortener/tree/master/core/static/img/screenshot/screenshot.png)


## Instalação

1. Faça o clone do projeto:

```bash
$ git clone https://github.com/alisonamerico/django-url-shortener.git
```

2. Crie um ambiente virtualizado com [virtualenv]() e ative-o:

```bash
$ cd django-url-shortener
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Executando o último comando, deve aparecer dessa forma:

```bash
(.venv)$
```

Isso significa que o ambiente foi ativado com sucesso. Agora vamos instalar as dependências:

```bash
(.venv)$ pip install -r requirements.txt
```

Ele vai fazer o download do pacote. Deve aparecer dessa forma:

```bash
Collecting django
  Downloading Django-1.11-py2.py3-none-any.whl (6.6MB)
    100% |████████████████████████████████| 6.6MB 193kB/s
Installing collected packages: django
Successfully installed django-1.11
```


3. Rode o comando abaixo para o Django criar novas migrações com base nas mudanças que você fez em seus modelos:

```bash
(.venv)$ python manage.py makemigrations
```

4. Rode o comando abaixo para aplicar e migrar as migrações:

```bash
(.venv)$ python manage.py migrate
```

5. Agora rode o projeto com o servidor embarcado:

```bash
(.venv)$ python manage.py runserver
```

6. Acesse o sistema em `http://localhost:8000` e o painel do administrador em `http://localhost:8000/admin`

7. Para executar os testes automatizados, no caso da versão standalone:

```bash
(.venv)$ python manage.py test
```

## Dúvidas ou problemas

Em caso de dúvidas ou problemas para configurar e rodar o projeto, crie uma [Issue](https://github.com/alisonamerico/django-url-shortener/issues) nesse repositório.
