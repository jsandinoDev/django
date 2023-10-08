# Iniciar Ambiente virtual en VSCode

py -3 -m venv .venv .venv\scripts\activate

# Instalar python
python -m pip install django

# Version
django-admin version    

# Crear projecto
django-admin startproject sap  

# Run Server
python manage.py runserver

# Migraciones
python manage.py showmigrations
python manage.py migrate
## Despues de crear un modelo
python manage.py makemigrations 
## Para crearlo despues (el 0001 fue el archivo creado en migrations)
python manage.py sqlmigrate personas 0001
## Para aplicar todas las migraciones pendientes
python manage.py migrate


# Instalar postgress
python -m pip install psycopg2  

configurar el archivo setting.py
DATABASES
