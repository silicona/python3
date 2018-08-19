from django.conf.urls import url
from django.contrib.auth import views as acceso

from . import views


urlpatterns = [
	url( r'^$', views.ver_todos, name = 'listado' ),
	url( r'^nuevo/$', views.crear, name = 'crear' ),
	url( r'^borradores/$', views.ver_borradores, name = 'borradores' ),
	url( r'^(?P<pk>[0-9]+)/$', views.ver_post, name = 'detalle' ),
	url( r'^(?P<pk>[0-9]+)/editar/$', views.editar, name = 'editar' ),
	url( r'^(?P<pk>[0-9]+)/publicar/$', views.publicar_post, name = 'publicar_post' ),
	url( r'^(?P<pk>[0-9]+)/borrar/$', views.borrar, name = 'borrar' ),

	url( r'^acceder/$', acceso.LoginView.as_view(), name = 'acceder' ),
	url( r'^salir/$', acceso.LogoutView.as_view(), name = 'salir' ),

	url( r'^(?P<pk>[0-9]+)/comentar/$', views.comentar, name = 'comentar' ),
	url( r'^(?P<pk>[0-9]+)/aprobar/$', views.aprobar, name = 'aprobar_comentario' ),
	url( r'^(?P<pk>[0-9]+)/rechazar/$', views.rechazar, name = 'rechazar_comentario' ),
]