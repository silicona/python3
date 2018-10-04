# Readme

App de prueba de django creada desde Tutorial y Tutorial 2 - blog_app.

[Documentacion 2.1](https://docs.djangoproject.com/es/2.1/)

[Tutorial](https://djangotutorial.readthedocs.io/es/1.8/intro/tutorial01.html)

[Tutorial 2](https://tutorial.djangogirls.org/es/django_urls/)


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


	### Interface Admin

		Instalar `pip3 install mysqlclient`

		Migrar la base de datos: `python3 manage.py migrate`

		Posibilidad de crear un nuevo superusuario: `python3 manage.py createsuperuser`

		Creacion de superusuario: usuario.

		Añadido Extra para interface Admin en urls.py

		Abrir consola de bpython por django:
		  : `python3 manage.py shell`


## Crear una aplicación del proyecto

	En consola desde el root: `python3 manage.py startapp <nombre_app>`

	Creacion de la subcarpeta <nombre_app>:
		: __init__.py - Package
		: admin.py - Modifica la app desde el interface Admin
		: models.py - Modelos de la app
		: tests.py - Tests de la app
		: views.py - Pues eso

	Registrar la app en settings.py (tuple INSTALLED_APPS):
		: Añadir `...'django.contrib.staticfiles', '<nombre_app>')`


	### Modelos

		Preparar migración de app:
		  : `python3 manage.py makemigrations <nombre_app>`

		Ejecuta las migraciones pendientes:
		  : `python3 manage.py migrate`


		Devuelve la SQL de la migracion (como dry-run):
		  : `python3 manage.py sqlmigrate <nombre_app> <nombre_migracion>`


		#### Jugando con la API de Django (modelos y bbdd)

			Abrir consola bpython de django

			`>> from encuestas_app.models import Pregunta, Eleccion`

			`>> Pregunta.objects.all()`

			-> [] - Resultado en array

			`>> from django.utils import timezone`

			`>> p = Pregunta( pregunta_texto = "¿Y ahora qué?", f_pub = timezone.now() )`

			`>> p.save()`

			>>> from polls.models import Pregunta, Eleccion

			# Make sure our __str__() addition worked.
			>>> Pregunta.objects.all()
			[<Pregunta: What's up?>]

			# Django provides a rich database lookup API that's entirely driven by keyword arguments.
			>>> Pregunta.objects.filter(id=1)
			[<Pregunta: What's up?>]
			>>> Pregunta.objects.filter(Pregunta_text__startswith='What')
			[<Pregunta: What's up?>]

			# Get the Pregunta that was published this year.
			>>> from django.utils import timezone
			>>> current_year = timezone.now().year
			>>> Pregunta.objects.get(f_pub__year = current_year)
			<Pregunta: What's up?>

			# Request an ID that doesn't exist, this will raise an exception.
			>>> Pregunta.objects.get(id=2)
			Traceback (most recent call last):
			    ...
			DoesNotExist: Pregunta matching query does not exist.

			# Lookup by a primary key is the most common case, so Django provides a
			# shortcut for primary-key exact lookups.
			# The following is identical to Pregunta.objects.get(id=1).
			>>> Pregunta.objects.get(pk=1)
			<Pregunta: What's up?>

			# Make sure our custom method worked.
			>>> q = Pregunta.objects.get(pk=1)
			>>> q.was_published_recently()
			True

			# Give the Pregunta a couple of Eleccions. The create call constructs a new
			# Eleccion object, does the INSERT statement, adds the eleccion to the set
			# of available eleccions and returns the new Eleccion object. Django creates
			# a set to hold the "other side" of a ForeignKey relation
			# (e.g. a Pregunta's eleccion) which can be accessed via the API.
			>>> q = Pregunta.objects.get(pk=1)

			# Display any eleccions from the related object set -- none so far.
			>>> q.eleccion_set.all()
			[]

			# Create three eleccions.
			>>> q.eleccion_set.create(eleccion_text='Not much', votes=0)
			<Eleccion: Not much>
			>>> q.eleccion_set.create(eleccion_text='The sky', votes=0)
			<Eleccion: The sky>
			>>> c = q.eleccion_set.create(eleccion_text='Just hacking again', votes=0)

			# Eleccion objects have API access to their related Pregunta objects.
			>>> c.Pregunta
			<Pregunta: What's up?>

			# And vice versa: Pregunta objects get access to Eleccion objects.
			>>> q.eleccion_set.all()
			[<Eleccion: Not much>, <Eleccion: The sky>, <Eleccion: Just hacking again>]
			>>> q.eleccion_set.count()
			3

			# The API automatically follows relationships as far as you need.
			# Use double underscores to separate relationships.
			# This works as many levels deep as you want; there's no limit.
			# Find all Eleccions for any Pregunta whose f_pub is in this year
			# (reusing the 'current_year' variable we created above).
			>>> Eleccion.objects.filter(Pregunta__pub_date__year=current_year)
			[<Eleccion: Not much>, <Eleccion: The sky>, <Eleccion: Just hacking again>]

			# Let's delete one of the eleccions. Use delete() for that.
			>>> c = q.eleccion_set.filter(eleccion_text__startswith='Just hacking')
			>>> c.delete()


	### Vistas

		[Documentacion filters construidos](https://docs.djangoproject.com/es/2.1/ref/templates/builtins/)
		Filtros de texto:
		  : `{{ texto|linebreaksbr }}`

		  
	### Admin

		Añadir la app al Admin para modificarlo desde su pantalla:
		  : (en encuestas_app/admin.py) - `from .models import Pregunta \ admin.site.register( Pregunta )`

		  : Agregado clase PreguntaAdmin para personalizar el modelo en el admin, incluyendo Eleccion

		  : Agregamos 'APP_DIRS' en settings.py 
		  : Modificar el template de Admin en carpeta root/templates, para que todos los templates esten accesibles al proyecto.


	### Tests

		Creacion de test en encuestas_app/tests.py

		Ejecución de tests desde consola: `python3 manage.py test encuestas_app`

			#### Jugando con la API de Django para tests - Client

				`>> from django.test.utils import setup_test_environment`
				`>> setup_test_environment()` - Renderizador de templates (response.context y otras variables)

				Uso desde cero - Al importar test.TestCase, trae su propio cliente
				`>>> from django.test import Client`
				`>>> # create an instance of the client for our use`
				`>>> client = Client()`
				Con eso listo, podemos pedirle al cliente que haga trabajo por nosotros:

				`>>> # get a response from '/'`
				`>>> response = client.get('/')`
				`>>> # we should expect a 404 from that address`
				`>>> response.status_code`
				404
				>>> # on the other hand we should expect to find something at '/polls/'
				>>> # we'll use 'reverse()' rather than a hardcoded URL
				`>>> from django.core.urlresolvers import reverse`
				`>>> response = client.get(reverse('polls:index'))`
				`>>> response.status_code`
				200
				`>>> response.content`
				'\n\n\n    <p>No polls are available.</p>\n\n'
				>>> # note - you might get unexpected results if your ``TIME_ZONE``
				>>> # in ``settings.py`` is not correct. If you need to change it,
				>>> # you will also need to restart your shell session
				`>>> from polls.models import Question`
				`>>> from django.utils import timezone`
				>>> # create a Question and save it
				`>>> q = Question(question_text="Who is your favorite Beatle?", pub_date=timezone.now())`
				`>>> q.save()`
				>>> # check the response once again
				`>>> response = client.get('/polls/')`
				`>>> response.content`
				'\n\n\n    <ul>\n    \n        <li><a href="/polls/1/">Who is your favorite Beatle?</a></li>\n    \n    </ul>\n\n'
				>>> # If the following doesn't work, you probably omitted the call to
				>>> # setup_test_environment() described above
				`>>> response.context['latest_question_list']`
				[<Question: Who is your favorite Beatle?>]

			#### Cobertura de codigo en tests

				Instalar con pip coverage

				[Documentacion](https://coverage.readthedocs.io/en/coverage-4.5.1a/)

				Ejecutar desde consola: `coverage run --source='.' manage.py test <nombre_app>`

				Obtener informe de cobertura: `coverage report`


	### Convertir una App en Paquete independiente

		[Tutorial 1.8](https://djangotutorial.readthedocs.io/es/1.8/intro/reusable-apps.html)


## Blog App

[Origen](https://tutorial.djangogirls.org/es/django_models/)

## Debug en Django

	### PDB

		Debugger de Python:
		  : Ejecutar desde consola: `python3 -m pdb manage.py runserver` - Duda de efectividad
		  : Establecer punto de ruptura: `import pdb; pdb.set_trace()` - Efectivo a solas

		[Documentacion PDB](https://docs.python.org/3/library/pdb.html#debugger-commands)




