# Readme

[Tutorial](https://djangotutorial.readthedocs.io/es/1.8/intro/tutorial01.html)

## Encuestas_app

Modelos Pregunta y Eleccion en encuestas_app/models.py

### Jugando con la API de Django

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


## Admin

Añadir la app al Admin para modificarlo desde su pantalla:
  : (en encuestas_app/admin.py) - `from .models import Pregunta \ admin.site.register( Pregunta )`

  : Agregado clase PreguntaAdmin para personalizar el modelo en el admin, incluyendo Eleccion

  : Agregamos 'APP_DIRS' en settings.py 
  : Modificar el template de Admin en carpeta root/templates, para que todos los templates esten accesibles al proyecto.

