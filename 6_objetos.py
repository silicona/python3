#!usr/bin/python3
# -*- coding:utf-8 -*-

def oir():

	pass


class Objeto(object):	# Hereda de object

	color = "verde"	# Atributo
	aspecto = 'feo'	

	oidos = oir()	# Propiedad
	
	def flotar(self):

		return "Yo floto"


class NuevoObjeto(Objeto):

	pie = 2

	def saltar( self ):

		return "\tTengo {} pies".format(self.pie)

print("\nObjeto heredado de object")

objeto = Objeto()

print( "\tColor de objeto: " + objeto.color )

variable = objeto.flotar()

print( "\tVariable: " + variable )

contenedor = objeto.flotar

print( "\tContenedor: ", contenedor() )

nuevo_objeto = NuevoObjeto();

print( nuevo_objeto.saltar() )

print( "\nPropiedades" )

print( "Las propiedades de las clases son atributos que manejamos con el uso de getter, setter y deleter, por lo que estos atributos pueden ser llamados “atributos manejados” y pueden ser considerados atributos especiales.La función property() que se encuentra integrada en el intérprete, nos va a permitir canalizar la escritura, lectura de los atributos.")

class Persona:

	def __init__( self, nombre ):

		self.set_nombre = nombre

	def get_nombre( self ):

		try:
			print( "Pedimos atributo" )

			return self.__nombre

		except AttributeError as error:

			print( "\tCazado: Error al acceder al atributo: ", error )


	def set_nombre( self, nuevo_nombre ):

		print( "Asignamos el valor", nuevo_nombre, "al atributo 'nombre'")

		self.__nombre = nuevo_nombre

		return None


	def del_nombre( self ):

		try:
			print( "Borramos atributo", self.__nombre )
			del self.__nombre
		
		except AttributeError:
		
			print( "Error: No existe el atributo que desea borrar" )

		except:

			print( "Error al intentar borrar el atributo" )

		return None

	nombre = property( get_nombre, set_nombre, del_nombre, "Mi información" )

def main():

	print("\nDesde Main()")
	a = Persona( "Pepe" )
	a.nombre = "Juan"

	print( a.nombre )
	del a.nombre

	print( a.nombre )
	a.nombre = "Elena"
	print( a.nombre )

	# print( help(Persona.nombre) ) # Ejecuta el comando de bash help

main()

print( "\nMetaclases")
print( "\tTipo de la clase persona", type(Persona) )

# Equivalente a la creacion tradicional de clases
miPersona = type( 'miPersona', (), {'a': True} )

class miPersonatradicional(object):

	a = True


print( "\nClases Abstractas")
print( "\nMi parque automovilístico con metaclase ABCMeta")

import abc 	# Siglas de abstract base classes
from abc import ABCMeta

class Vehiculo(metaclass = ABCMeta):

	__metaclass__ = ABCMeta

	@abc.abstractmethod
	def quien_eres( self ):

		print( "\tSoy un vehiculo y un metodo abstracto." )


try:
	print("\nInstancianciando directamente de metaclase Vehiculo.")
	coche = Vehiculo()
	coche.quien_eres()

except Exception as error:

	print( "\tCazada: " + str(error) )


class Coche(Vehiculo):

	def quien_eres( self ):		

		print( "\tSoy un coche" )

		print( "Utilizando super.metodo_abstracto" )

		super().quien_eres()	
		
print( "\nInstanciando de clase heredera de Vehiculo")

coche = Coche()
coche.quien_eres()


print( "\nMi zoo" )
print( "Desde https://pythonista.io/cursos/py111/clases-abstractas-y-duck-typing" )

class Animal:
	''' Clase base de los animales'''

	def __init__( self, nombre ):

		self.nombre = nombre
		print( "\tHola. Mi nombre es {}, primate.".format(self.nombre) )


	def reproduccion(self):

		# Solo define una interfaz
		pass


	def alimentacion(self):

		# Solo define una interfaz
		pass


	def __del__(self):

		print( "\tEl animal {} ha fallecido, patético humano." )

class Mamifero(Animal):
	''' Clase con actividsades de mamiferos '''

	def reproduccion(self):

		''' Implementa la interfa<z reproduccion de la superclase '''
		print( "\tUn nuevo cachorro ha llegado, peludo simio." )


	def amamanta(self):

		print( "\tAmamanta al cachorro o morirá, ignorante bípedo.")


class Perro(Mamifero):

	def alimentacion(self):

		''' Implementa la interfaz allimentacion de la superclase '''
		print( "\tCerebro de pasa, ¿Solo entiendes que no puedo comer tornillos si te lo sigo con letras?" )


perro = Perro( 'Shilum' )

perro.alimentacion()

del perro

bicho = Mamifero( 'Cosa' )

bicho.alimentacion()

del bicho


print( "\nDuck Typing" )
print( "Cualquier clase que tenga una interfaz compatible puede interactuar con cualquier otra clase\n" )

# Clases Base
class EnergiaSolar:

	''' Clase base para las variedades de producción solar '''
	fuente = 'luz solar'

	def energia(self):
		pass


class EnergiaDinamica:

	''' Clase base para las variedades de producción mecánica '''
	fuente = 'Movimiento mecánico'

	def energia(self):
		pass

# Clases de herencia
class FotoVoltaica(EnergiaSolar):

	rendimiento = 500

	def __init__(self, lumenes):
		self.lumenes = lumenes

	def energia(self):
		return( self.lumenes * self.rendimiento, "watts/hr" )

class HidroElectrica(EnergiaDinamica):

	rendimiento = 2000

	def __init__(self, litros):
		self.litros = litros

	def energia(self):
		return( self.litros * self.rendimiento, 'watts/hr' )

# Clase que define un interfaz en el metodo __init__
class Dispositivo:

	def __init__(self, consumo = 50):
		self.consumo = float( consumo )

	def duracion(self, energia):
		
		'''El argumento para el parámetro energía debe de ser una lista o tulpa con 2 elementos 
		en los que el primer elemento debe de ser un número real y el segundo elemento debe 
		de ser la cadena de caracteres "watts/hr". '''
		
		if type(energia) in (tuple, list) and len(energia) == 2 and type(energia[0]) in (int, float) \
			and energia[1].casefold() == "watts/hr":

			return energia[0] / self.consumo

		else:

			raise ValueError('Interfaz incorrecta, mezquino humano.')


tostadora = Dispositivo( 20 )

luz = tostadora.duracion( FotoVoltaica(500).energia() )
print( "\t-Energia solar: ", luz )

agua = tostadora.duracion( HidroElectrica(500).energia() )
print( "\t-Energia acuosa: ", agua )


print( "\nZOPE" )
print( "Comentado - solo python 2, o eso dicen" )

print( "Instalar con pip install zope, ejecutar como python2 y probar este script" )

print( "No deja instalar zope por pip en linux" )

# from zope.interface import Interface, Attribute, implements

# class IFoo(interface):

# 	def saludo():
# 		print( "Hola")


# class Foo(object):

# 	implements(IFoo)

# 	def __init__( self, otro = "Mundo" ):
# 		self.otro = otro

# 	def saludo(self):
# 		print "Hola", self.otro

# saludo = Foo()

# saludo.saludo()

print( "\nSobrecarga de operadores" )
print( "Métodos mágicos de Python3: https://www.python-course.eu/python3_magic_methods.php")

print( "\nEjemplo con clase Circulo(add)")

import math

class Circulo:

	def __init__( self, radio ):
		self.__radio = radio

	def setRadio( self, radio ):
		self.__radio = radio

	def getRadio(self):
		return self.__radio

	def area(self):
		return math.pi *self__radio ** 2

	def __add__(self, otro_circulo):
		return Circulo( self.__radio + otro_circulo.__radio )

c1 = Circulo(4)
print( "\tRadio c1", c1.getRadio() )

c2 = Circulo(5)
print( "\tRadio c2", c2.getRadio() )

c3 = c1 + c2
print( "\tRadio c3", c3.getRadio() )


print( "\n Ejemplo con clase Devuelta (str)")

class Devuelta:

	x = 2
	y = 3

	def __str__(self):
		''' Muestra el punto como par ordenado '''
		return "(" + str(self.x) + ", " + str(self.y) + ")"


devuelta = Devuelta()

print( "\tDevuelta: ", devuelta )


print( "\nEjemplo con Clase Longitud (add, str, repr)")

class Longitud:

    __metrica = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344 }
    
    def __init__(self, valor, unidad = "m" ):
        self.valor = valor
        self.unidad= unidad
    
    def Converse2Metres(self):
        return self.valor * Longitud.__metrica[self.unidad]
    
    def __add__(self, other):
        l = self.Converse2Metres() + other.Converse2Metres()
        return Longitud(l / Longitud.__metrica[self.unidad], self.unidad )
    
    def __str__(self):
        return str(self.Converse2Metres())
    
    def __repr__(self):
        return "Longitud(" + str(self.valor) + ", '" + self.unidad + "')"

if __name__ == "__main__":

    x = Longitud(4)
    print( "\tX: ", x )

    y = eval( repr(x) )
    print( "\tY: ", y )

    z = Longitud(4.5, "yd") + Longitud(1)
    print("\tRepr de z: ", repr(z))
    print("\tZ: ", z)


print( "\nCódigo para importar Longitud desde unit_conversions.py (ficticio)" )
# from unit_conversions import Length

# L = Length

# print( L(2.56,"m") + L(3,"yd") + L(7.8,"in") + L(7.03,"cm") )