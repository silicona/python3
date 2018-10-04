# Readme

App de prueba de django creada desde la app movil Learn Django

## Instalación

Instalar Django: `pip3 install django`

Comprobar la instalacion correcta viendo la version de Django: `django-admin.py --version`

## Crear nuevo proyecto

Crear proyecto (carpeta nueva): `django-admin startproyect <nombre_app>`

Ayuda de consola de Django (en consola): `python manage.py help`
	: manage.py - Interacción con el proyecto por consola
	: Subcarpeta <nombre_app>:
	  : __init__.py - Package
	  : settings.py - 
	  : urls.py - Router
	  : wsgi.py - Para subirlo a producción con WSGI

### Settings

Opcion importante: `DEBUG = True` - Solo para Dev

Añadir las propiedades USER, PASSWORD, HOST, PORT en DATABASES

Comprobar la creación correcta: `python3 manage.py runserver`

## Crear la aplicación

En consola desde el root: `python3 manage.py startapp mi_app`

Creacion de la subcarpeta 'mi_app':
	: __init__.py - Package
	: admin.py - Modifica la app desde el interface Admin
	: models.py - Modelos de la app
	: tests.py - Tests de la app
	: views.py - Pues eso

Registrar la app en settings.py (tuple INSTALLED_APPS):
	: Añadir `...'django.contrib.staticfiles', 'mi_app')`

## Interface Admin

Instalar `pip3 install mysqlclient`

Migrar la base de datos: `python3 manage.py migrate`

Posibilidad de crear un nuevo superusuario: `python3 manage.py createsuperuser`

Creacion de superusuario: usuario.

Añadido Extra para interface Admin en urls.py

Abrir consola de bpython por django:
  : `python3 manage.py shell`


## Modelos

Preparar migración de app:
  : `python3 manage.py makemigrations <nombre_app>`

Ejecuta las migraciones pendientes:
  : `python3 manage.py migrate`


Devuelve la SQL de la migracion (como dry-run):
  : `python3 manage.py sqlmigrate <nombre_app> <nombre_migracion>`


### Jugando con la API de Django

Abrir consola bpython de django

`>> from encuestas_app.models import Pregunta, Eleccion`

`>> Pregunta.objects.all()`

-> [] - Resultado en array

`>> from django.utils import timezone`

`>> p = Pregunta( pregunta_texto = "¿Y ahora qué?", f_pub = timezone.now() )`

`>> p.save()`