from django.conf.urls import url

from . import views

urlpatterns = [


    # FACTORIZACION PARA VISTAS CON GENERIC
	url( r'^$', views.IndexView.as_view(), name = "index" ),
	url( r'^(?P<nombre>[^0-9]+)$', views.IndexView.as_view(), name = "index" ),
    # DetailView espera el valor de clave primaria capturado de la URL con nombre \"pk\"
    url( r'^(?P<pk>[0-9]+)/$', views.DetalleView.as_view(), name='detalle'),
    url( r'^(?P<pk>[0-9]+)/resultados/$', views.ResultadosView.as_view(), name='resultados'),


	# /encuestas/
	# url( r'^$', views.index, name = "index" ),
	# /encuestas/nombre
	# url( r'^(?P<nombre>[^0-9]+)$', views.index, name = "index" ),
    # # /encuestas/5/
    # url( r'^(?P<pregunta_id>[0-9]+)/$', views.detalle, name='detalle'),
    # # /encuestas/5/resultados/
    # url( r'^(?P<pregunta_id>[0-9]+)/resultados/$', views.resultados, name='resultados'),
    
    # # /encuestas/5/votar/
    url( r'^(?P<pregunta_id>[0-9]+)/votar/$', views.votar, name='votar'),
]