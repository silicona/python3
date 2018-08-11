#!usr/bin/python
# -*- coding:utf-8 -*-

# No permite instalar zope por pip en Linux
from zope.interface import Interface, Attribute, implements

class IFoo(interface):

	def saludo():
		print( "Hola")


class Foo(object):

	implements(IFoo)

	def __init__( self, otro = "Mundo" ):
		self.otro = otro

	def saludo(self):
		print "Hola", self.otro

print "\nInterfaz ZOPE"

saludo = Foo()

saludo.saludo()