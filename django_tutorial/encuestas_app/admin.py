from django.contrib import admin

# Register your models here.
from .models import Pregunta, Eleccion

# class EleccionEnLinea( admin.StackedInline ):	# Visualizacion en bloques
class EleccionEnLinea( admin.TabularInline ):	# Visualizacion más compacta

	model = Eleccion
	extra = 3	# Cantidad inicial de elecciones en pantalla


class PreguntaAdmin( admin.ModelAdmin ):

	# campos = ['f_pub', 'pregunta_texto']	# Orden de los campos en Admin
	fieldsets = [
		( None, {'fields': ['pregunta_texto']} ),
		( 'Información', {'fields': ['f_pub'], 'classes': ['collapse']} )
	]

	inlines = [EleccionEnLinea]		# Añadido en linea de las Elecciones de cada pregunta

	list_display = ('pregunta_texto', 'f_pub', 'recien_publicada')	# Orden de campos en vista de Pregunta 

	list_filter = ['f_pub']		# Celda a la que se aplica el desplegable de filtro

	search_field = ['pregunta_texto']	# Celda con campo de busqueda



admin.site.register( Pregunta, PreguntaAdmin )
