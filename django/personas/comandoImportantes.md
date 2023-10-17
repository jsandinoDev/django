# Iniciar Ambiente virtual en VSCode

py -3 -m venv .venv 
# Seleccionar el python interpreter (debe ser el VENV)
control + shift + p


# Instalar python
python -m pip install django

# Version
django-admin version    

# Crear projecto
django-admin startproject sap  

# Crear app
pyhton manage.py startapp personas

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

# configurar el archivo setting.py
DATABASES

# La carpeta "base"del proyecto es
SAP



# Crear archivo de dependecias (venv/lib/etc)
pip freeze > requirements.txt
# Usar el archivo creado anteriormente 
pip install -r requirements.txt