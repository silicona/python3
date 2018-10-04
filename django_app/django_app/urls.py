"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import *
from django.urls import path

urlpatterns = [

	path( r'^$', mi_app.views.saludo ),
    path( r'^admin/', admin.site.urls ),
]

# # Extras de tutorial movil
# from django.urls import include
# from django.conf.urls import include, url

# # # admin.autodiscover()
# urlpatterns = [
# 	'',
# 	# Examples:
# 	# url( r'^$', 'django_app.views.home' ),
# 	# url( r'^blog/', include('blog.urls') ),
# 	url( "admin/", admin.site.urls ),
# ]
