from django.contrib import admin

from .models import *

# Register your models here.

class PostEnLinea(admin.StackedInline):

	model = Post
	extra = 1


class UsuarioAdmin(admin.ModelAdmin):

	# fielsets = [
	# 	( None, {'fields': ['nombre']} ),
	# ]

	inlines = [PostEnLinea]

	

admin.site.register( Usuario )
admin.site.register( Post )
admin.site.register( Comentario )