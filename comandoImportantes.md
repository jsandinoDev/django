# DJANGO WIKI


##  Instalar python
```
python -m pip install django
```

##  Version
```
django-admin version    
```
# Pip File
###  Crear archivo de dependecias (venv/lib/etc)
```
pip freeze > requirements.txt
```

###  Usar el archivo creado anteriormente 
```
pip install -r requirements.txt
```

# Ambiente Virtual
###  Iniciar Ambiente virtual en VSCode
```
py -3 -m venv .venv 
```

###  Seleccionar el python interpreter (debe ser el VENV)
```
control + shift + p
```
## Comandos creacion projectos
### Crear projecto
```
django-admin startproject sap  
```

###  Crear app
```
pyhton manage.py startapp personas
```
##  Run Server
```
python manage.py runserver
```

##  Migraciones
```
python manage.py showmigrations
python manage.py migrate
```
### Despues de crear un modelo
```
python manage.py makemigrations 
```
### Para crearlo despues (el 0001 fue el archivo creado en migrations)
```
python manage.py sqlmigrate personas 0001
```
### Para aplicar todas las migraciones pendientes
```
python manage.py migrate
```

##  Instalar postgress
```
python -m pip install psycopg2  
```

##  configurar el archivo setting.py
```
DATABASES
```

##  La carpeta "base"del proyecto es
```
SAP
```

##  Crear super usuario
```
pyhton manage.py createsuperuser
admin
123
```

##  Usar la consola de admin de django
```
en la clase del modelo agregar en admin
$ admin.site.register(Persona)
```