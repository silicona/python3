from django.conf.urls import url

from . import views

urlpatterns = [

	# ex: /encuestas/
	url( r'^$', views.index, name = "index" ),

	# ex: /polls/nombre
	url( r'^(?P<nombre>[^0-9]+)$', views.index, name = "index" ),

	# ex: /polls/5/
    url( r'^(?P<pregunta_id>[0-9]+)/$', views.detalle, name='detalle'),
    
    # ex: /polls/5/results/
    url( r'^(?P<pregunta_id>[0-9]+)/resultados/$', views.resultados, name='resultados'),
    
    # ex: /polls/5/vote/
    url( r'^(?P<pregunta_id>[0-9]+)/votar/$', views.votar, name='votar'),
]