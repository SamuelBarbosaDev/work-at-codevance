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

## Deploy:
- instalando a lib:
```
sudo apt install heroku
```

- Faça o login:
```
heroku login
```

- Crie um app:
```
heroku create work-at-codevance-samuel
```

## URLS:

- Home:
```
http://127.0.0.1:8000/
```

- history:
```
http://127.0.0.1:8000/core/history/
```

- payments:
```
http://127.0.0.1:8000/core/payments/
```

- requests:
```
http://127.0.0.1:8000/core/requests/
```

### API:

- Api:
```
http://127.0.0.1:8000/api/
```

- Documentação da Api:
```
http://127.0.0.1:8000/api/docs/
```

## Estrutura de pasta:

```
├── apps
│   ├── celery.py
│   ├── conftest.py
│   ├── contrib
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   └── __init__.cpython-310.pyc
│   │   └── sites
│   │       ├── __init__.py
│   │       ├── migrations
│   │       │   ├── 0001_initial.py
│   │       │   ├── 0002_alter_domain_unique.py
│   │       │   ├── 0003_set_site_domain_and_name.py
│   │       │   ├── 0004_alter_options_ordering_domain.py
│   │       │   ├── __init__.py
│   │       │   └── __pycache__
│   │       │       ├── 0001_initial.cpython-310.pyc
│   │       │       ├── 0002_alter_domain_unique.cpython-310.pyc
│   │       │       ├── 0003_set_site_domain_and_name.cpython-310.pyc
│   │       │       ├── 0004_alter_options_ordering_domain.cpython-310.pyc
│   │       │       └── __init__.cpython-310.pyc
│   │       └── __pycache__
│   │           └── __init__.cpython-310.pyc
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── celery.cpython-310.pyc
│   │   ├── conftest.cpython-310-pytest-7.1.3.pyc
│   │   └── __init__.cpython-310.pyc
│   ├── static
│   │   ├── css
│   │   │   └── project.css
│   │   ├── fonts
│   │   ├── images
│   │   │   └── favicons
│   │   │       └── favicon.ico
│   │   └── js
│   │       └── project.js
│   ├── templates
│   │   ├── 403.html
│   │   ├── 404.html
│   │   ├── 500.html
│   │   ├── account
│   │   │   ├── account_inactive.html
│   │   │   ├── base.html
│   │   │   ├── email_confirm.html
│   │   │   ├── email.html
│   │   │   ├── login.html
│   │   │   ├── logout.html
│   │   │   ├── password_change.html
│   │   │   ├── password_reset_done.html
│   │   │   ├── password_reset_from_key_done.html
│   │   │   ├── password_reset_from_key.html
│   │   │   ├── password_reset.html
│   │   │   ├── password_set.html
│   │   │   ├── signup_closed.html
│   │   │   ├── signup.html
│   │   │   ├── verification_sent.html
│   │   │   └── verified_email_required.html
│   │   ├── base.html
│   │   ├── pages
│   │   │   ├── about.html
│   │   │   └── home.html
│   │   └── users
│   │       ├── user_detail.html
│   │       └── user_form.html
│   ├── users
│   │   ├── adapters.py
│   │   ├── admin.py
│   │   ├── api
│   │   │   ├── __pycache__
│   │   │   │   ├── serializers.cpython-310.pyc
│   │   │   │   └── views.cpython-310.pyc
│   │   │   ├── serializers.py
│   │   │   └── views.py
│   │   ├── apps.py
│   │   ├── context_processors.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── 0001_initial.cpython-310.pyc
│   │   │       └── __init__.cpython-310.pyc
│   │   ├── models.py
│   │   ├── __pycache__
│   │   │   ├── adapters.cpython-310.pyc
│   │   │   ├── admin.cpython-310.pyc
│   │   │   ├── apps.cpython-310.pyc
│   │   │   ├── context_processors.cpython-310.pyc
│   │   │   ├── forms.cpython-310.pyc
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── models.cpython-310.pyc
│   │   │   ├── tasks.cpython-310.pyc
│   │   │   ├── urls.cpython-310.pyc
│   │   │   └── views.cpython-310.pyc
│   │   ├── tasks.py
│   │   ├── tests
│   │   │   ├── factories.py
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── factories.cpython-310.pyc
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── test_admin.cpython-310-pytest-7.1.3.pyc
│   │   │   │   ├── test_drf_urls.cpython-310-pytest-7.1.3.pyc
│   │   │   │   ├── test_drf_views.cpython-310-pytest-7.1.3.pyc
│   │   │   │   ├── test_forms.cpython-310-pytest-7.1.3.pyc
│   │   │   │   ├── test_models.cpython-310-pytest-7.1.3.pyc
│   │   │   │   ├── test_swagger.cpython-310-pytest-7.1.3.pyc
│   │   │   │   ├── test_tasks.cpython-310-pytest-7.1.3.pyc
│   │   │   │   ├── test_urls.cpython-310-pytest-7.1.3.pyc
│   │   │   │   └── test_views.cpython-310-pytest-7.1.3.pyc
│   │   │   ├── test_admin.py
│   │   │   ├── test_drf_urls.py
│   │   │   ├── test_drf_views.py
│   │   │   ├── test_forms.py
│   │   │   ├── test_models.py
│   │   │   ├── test_swagger.py
│   │   │   ├── test_tasks.py
│   │   │   ├── test_urls.py
│   │   │   └── test_views.py
│   │   ├── urls.py
│   │   └── views.py
│   └── utils
│       └── __init__.py
├── config
│   ├── api_router.py
│   ├── celery_app.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── api_router.cpython-310.pyc
│   │   ├── celery_app.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── settings
│   │   ├── base.py
│   │   ├── __init__.py
│   │   ├── local.py
│   │   ├── production.py
│   │   ├── __pycache__
│   │   │   ├── base.cpython-310.pyc
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── local.cpython-310.pyc
│   │   │   └── test.cpython-310.pyc
│   │   └── test.py
│   ├── urls.py
│   └── wsgi.py
├── CONTRIBUTORS.txt
├── core
│   ├── admin.py
│   ├── api
│   │   ├── __pycache__
│   │   │   ├── serializers.cpython-310.pyc
│   │   │   └── views.cpython-310.pyc
│   │   ├── serializers.py
│   │   └── views.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20221020_0141.py
│   │   ├── 0003_alter_payments_original_value.py
│   │   ├── 0004_company.py
│   │   ├── 0005_alter_company_payments.py
│   │   ├── 0006_auto_20221020_1004.py
│   │   ├── 0007_auto_20221020_1011.py
│   │   ├── 0008_alter_company_requests.py
│   │   ├── 0009_payments_request_status.py
│   │   ├── 0010_alter_payments_request_status.py
│   │   ├── 0011_rename_company_request.py
│   │   ├── 0012_auto_20221020_1327.py
│   │   ├── 0013_supplier_user.py
│   │   ├── 0014_alter_supplier_user.py
│   │   ├── 0015_payments_user.py
│   │   ├── 0016_auto_20221021_1244.py
│   │   ├── 0017_auto_20221021_1321.py
│   │   ├── 0018_alter_payments_date_of_issue.py
│   │   ├── 0019_remove_payments_date_of_issue.py
│   │   ├── 0020_payments_date_of_issue.py
│   │   ├── 0021_alter_payments_date_of_issue.py
│   │   ├── 0022_request_date_of_issue.py
│   │   ├── 0023_request_user.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       ├── 0002_auto_20221020_0141.cpython-310.pyc
│   │       ├── 0003_alter_payments_original_value.cpython-310.pyc
│   │       ├── 0004_company.cpython-310.pyc
│   │       ├── 0005_alter_company_payments.cpython-310.pyc
│   │       ├── 0006_auto_20221020_1004.cpython-310.pyc
│   │       ├── 0007_auto_20221020_1011.cpython-310.pyc
│   │       ├── 0008_alter_company_requests.cpython-310.pyc
│   │       ├── 0009_payments_request_status.cpython-310.pyc
│   │       ├── 0010_alter_payments_request_status.cpython-310.pyc
│   │       ├── 0011_rename_company_request.cpython-310.pyc
│   │       ├── 0012_auto_20221020_1327.cpython-310.pyc
│   │       ├── 0013_supplier_user.cpython-310.pyc
│   │       ├── 0014_alter_supplier_user.cpython-310.pyc
│   │       ├── 0015_payments_user.cpython-310.pyc
│   │       ├── 0016_auto_20221021_1244.cpython-310.pyc
│   │       ├── 0017_auto_20221021_1321.cpython-310.pyc
│   │       ├── 0018_alter_payments_date_of_issue.cpython-310.pyc
│   │       ├── 0019_remove_payments_date_of_issue.cpython-310.pyc
│   │       ├── 0020_payments_date_of_issue.cpython-310.pyc
│   │       ├── 0021_alter_payments_date_of_issue.cpython-310.pyc
│   │       ├── 0022_request_date_of_issue.cpython-310.pyc
│   │       ├── 0023_request_user.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── __init__.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── tasks.cpython-310.pyc
│   │   ├── tests.cpython-310-pytest-7.1.3.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── tasks.py
│   ├── templates
│   │   └── core
│   │       └── pages
│   │           ├── history.html
│   │           ├── payments.html
│   │           └── requests.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── docs
│   ├── conf.py
│   ├── howto.rst
│   ├── index.rst
│   ├── __init__.py
│   ├── make.bat
│   ├── Makefile
│   └── users.rst
├── LICENSE
├── locale
│   └── README.rst
├── logs
│   └── logs.log
├── manage.py
├── merge_production_dotenvs_in_dotenv.py
├── Procfile
├── pytest.ini
├── README.md
├── requirements
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
├── requirements.txt
├── runtime.txt
├── setup.cfg
├── templates
│   └── base.html
└── utility
    ├── install_os_dependencies.sh
    ├── install_python_dependencies.sh
    ├── requirements-bionic.apt
    ├── requirements-bullseye.apt
    ├── requirements-buster.apt
    ├── requirements-focal.apt
    ├── requirements-jessie.apt
    ├── requirements-stretch.apt
    ├── requirements-trusty.apt
    └── requirements-xenial.apt

46 directories, 221 files
```