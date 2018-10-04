from django.db import models
from django.utils import timezone

# Create your models here: https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-types

class Usuario(models.Model):

	nombre   = models.CharField( max_length = 200 )
	email    = models.EmailField( max_length = 50 )
	usuario  = models.CharField( max_length = 20 )
	password = models.CharField( max_length = 20 )

	def __str__(self):

		return self.nombre



class Post(models.Model):

	autor  = models.ForeignKey( Usuario, on_delete = models.CASCADE )	
	titulo = models.CharField( max_length = 200 )
	texto  = models.TextField() 
	f_alta = models.DateTimeField( auto_now = True )
	f_pub  = models.DateTimeField( blank = True, null = True )


	def publicar(self):

		self.f_pub = timezone.now()
		self.save()


	def __str__(self):

		return self.titulo

	def eliminar(self):

		self.delete()

	def comentarios_aprobados(self):

		return self.comentarios.filter( aprobado = True )



class Comentario(models.Model):

	post     = models.ForeignKey( Post, on_delete = models.CASCADE, related_name = "comentarios" )
	autor    = models.ForeignKey( Usuario, on_delete = None )
	texto    = models.TextField()
	f_alta   = models.DateTimeField( auto_now = True )
	aprobado = models.BooleanField( default = False )

	def aprobar(self):

		self.aprobado = True
		self.save()


	def __str__(self):

		return self.texto


	def eliminar(self):

		self.delete()
