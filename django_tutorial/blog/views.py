from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import *

import time

from .models import *
# Create your views here.

def ver_todos( request ):

	# import pdb; pdb.set_trace()

	posts = Post.objects.filter( f_pub__lte = timezone.now() ).order_by('f_pub')

	return render( request, 'blog/listado.html', {'posts': posts, 'ano': time.strftime("%Y")} )


def ver_borradores( request ):

	posts = Post.objects.filter( f_pub__isnull = True ).order_by('f_alta')

	return render( request, 'blog/borradores.html', {'posts': posts, 'ano': time.strftime("%Y")})


def ver_post( request, pk ):

	post = get_object_or_404( Post, pk = pk )

	# import pdb; pdb.set_trace()
	return render( request, 'blog/detalle.html', {'post': post, 'ano': time.strftime("%Y")} )


@login_required
def crear( request ):


	if request.method == 'POST':

		form = FormPublicar( request.POST )
		if form.is_valid():

			post = form.save( commit = False )
			post.autor = Usuario.objects.get( pk = request.user.id )
			# post.f_pub = timezone.now()	# ELiminamos la publicacion automática para hacer borradores
			post.save()

			return redirect( 'blog:detalle', pk = post.pk )

	else:	

		form = FormPublicar()

	titulo = "Nueva publicación"
	return render( request, 'blog/publicar.html', {'form': form, 'titulo': titulo, 'ano': time.strftime("%Y")} )


@login_required
def editar( request, pk ):

	post = get_object_or_404( Post, pk = pk )

	if request.method == 'POST':

		form = FormPublicar( request.POST, instance = post )

		if form.is_valid():

			post = form.save( commit = False )
			post.autor = Usuario.objects.get( pk = request.user.id )
			post.save()

			return redirect( 'blog:detalle', pk = post.pk )

	else:

		form = FormPublicar( instance = post )

	titulo = "Editando publicación"
	return render( request, 'blog/publicar.html', {'form': form, 'titulo': titulo, 'ano': time.strftime("%Y")} )


@login_required
def publicar_post( request, pk ):

	post = get_object_or_404( Post, pk = pk )

	post.publicar()		# Metodo del modelo

	return redirect( 'blog:detalle', pk = post.pk)

@login_required
def borrar( request, pk ):

	post = get_object_or_404( Post, pk = pk )

	post.eliminar()

	return redirect( 'blog:listado' )


@login_required
def comentar( request, pk ):

	post = get_object_or_404( Post, pk = pk )

	if request.method == 'POST':

		form = FormComentar( request.POST )

		if form.is_valid():

			comentario = form.save( commit = False )
			comentario.autor = Usuario.objects.get( pk = request.user.pk )
			comentario.post = post
			comentario.save()

			return redirect( 'blog:detalle', pk = post.pk )

	else:

		form = FormComentar()

	return render( request, 'blog/comentar.html', {'form': form} )


@login_required
def aprobar( request, pk ):

	comentario = get_object_or_404( Comentario, pk = pk )

	comentario.aprobar()

	return redirect( 'blog:detalle', pk = comentario.post.pk )


@login_required
def rechazar( request, pk ):

	comentario = get_object_or_404( Comentario, pk = pk )

	comentario.elminar()

	return redirect( 'blog:detalle', pk = comentario.post.pk )


