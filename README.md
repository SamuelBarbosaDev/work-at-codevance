# Teste Técnico
### Ambiente virtual e Dependências:
- Criando ambiente virtual:
```
python -m venv venv
```

- Entrando no ambiente virtual:
```
source venv/bin/activate
```

- Entre na pasta app/:
```
cd apps/
```

- Instale as dependências:
```
pip install -r requirements/local.txt
```

### Criando banco de dados PostgreSQL:

- usuario postgres:
```
sudo -i -u postgres psql
```

- Crie o banco de dados:
```
CREATE DATABASE db;
```
- Depois, você modificará alguns dos parâmetros de conexão para o usuário que acabou de criar. Isso acelerará as operações do banco de dados para que os valores corretos não precisem ser consultados e definidos toda vez que uma conexão for estabelecida.

- Passo 1:
```
ALTER ROLE postgres SET client_encoding TO 'utf8';
```

- Passo 2:
```
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
```

- Passo 3:
```
ALTER ROLE postgres SET timezone TO 'UTC';
```

- Passo 4:
```
GRANT ALL PRIVILEGES ON DATABASE db TO postgres;
```

- Passo 5:
```
\q
```

### Execute as migrations:

- Execute as migrations:
```
python manage.py migrate
```

- Execute o servidor:
```
python manage.py runserver
```

## URLS: