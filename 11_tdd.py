#!usr/bin/python3
# -*- coding: utf-8 -*-

import math
import unittest
from tdd_func import *
from tdd_tests import RomanosTest

a = 9

# print( "1 - Opcion inuttest (class TddTestCase)" )

class Helper:

	@classmethod
	def crear_conexion_bbdd(clase):
		
		pass
	

class RectanguloTest( unittest.TestCase ):

	@classmethod
	def setUpClass(clase):

		clase._conexion = Helper.crear_conexion_bbdd()


	@classmethod
	def tearDownClass(clase):

		clase._conexion = False

	def setUpModule():

		print( "Inicio de modulo" )
		# pass

	def tearDownModule():

		print( "Fin de modulo" )
		# pass


	def setUp(self):

		self.rect = Rectangulo( 3, 5 )
		# self.rect_cuad = Rectangulo( 4, 4 )


	def tearDown(self):

		self.rect = False


	@unittest.skip('Mensaje de SKIP')
	def test_evitando_con_skip(self):

		self.assertTrue(True)


	@unittest.skipUnless(False, 'Mensaje de SKIP con unless')
	def test_evitando_con_skip_unless(self):

		self.assertTrue(True)


	'''
	url: https://docs.python.org/3/library/unittest.html#classes-and-functions

	assert: base assert allowing you to write your own assertions
	assertEqual(a, b): check a and b are equal (==)
	assertNotEqual(a, b): check a and b are not equal (!=)
	assertIn(a, b): check that a is in the item b (a in b)
	assertNotIn(a, b): check that a is not in the item b (a not in b)
	assertIs(a, b) 	a is b 	3.1
	assertIsNot(a, b) 	a is not b 	3.1
	assertIsNone(x) 	x is None 	3.1
	assertIsNotNone(x) 	x is not None 	3.1
	assertTrue(a): check the value of a is True (bool(a))
	assertFalse(a): check that the value of a is False (bool(a))
	assertIsInstance(a, TYPE): check that a is of type "TYPE" (isinstance(a, b))
	assertNotIsInstance(a, b): -	(not isinstance(a, b))
	assertRaises(ERROR, a, args): check that when a is called with args that it raises ERROR
	assertRaises(exc, fun, *args, **kwds): 	fun(*args, **kwds) raises exc 	 
	assertRaisesRegex(exc, r, fun, *args, **kwds): 	fun(*args, **kwds) raises exc and the message matches regex r
	assertWarns(warn, fun, *args, **kwds): 	fun(*args, **kwds) raises warn
	assertWarnsRegex(warn, r, fun, *args, **kwds): 	fun(*args, **kwds) raises warn and the message matches regex r
	assertLogs(logger, level): 	The with block logs on logger with minimum level
	assertAlmostEqual(a, b) 	round(a-b, 7) == 0 	 
	assertNotAlmostEqual(a, b) 	round(a-b, 7) != 0 	 
	assertGreater(a, b) 	a > b
	assertGreaterEqual(a, b) 	a >= b
	assertLess(a, b) 	a < b
	assertLessEqual(a, b) 	a <= b
	assertRegex(s, r) 	r.search(s)
	assertNotRegex(s, r) 	not r.search(s)
	assertCountEqual(a, b) 	a and b have the same elements in the same number, regardless of their order
	assertMultiLineEqual(a, b) 	strings 	3.1
	assertSequenceEqual(a, b) 	sequences 	3.1
	assertListEqual(a, b) 	lists 	3.1
	assertTupleEqual(a, b) 	tuples 	3.1
	assertSetEqual(a, b) 	sets or frozensets 	3.1
	assertDictEqual(a, b) 	dicts 	3.1
	'''

	def test_raiz(self):

		self.assertEqual( raiz_cuadrada(a), 3, 'La raiz no es 3' )


	def test_acelerar(self):

		self.assertEqual( acelerar(), 15, 'La velocidad no es 15' )


	def test_rectangulo(self):

		self.assertIsInstance( self.rect, (Rectangulo), 'La clase del ejemplo deberia ser Rectangulo' )
		self.assertIsInstance( self.rect, (Blob), 'La clase del ejemplo deberia ser Rectangulo' )


	def test_rectangulo_medir(self):

		self.assertTrue( self.rect.medir(3, 5), 'El rectángulo no tiene las medidas previstas' )


	def test_creacion_rectangulo(self):

		# rect = Rectangulo( 0, 0, 'red' );
		self.assertRaises( ValueError, Rectangulo.__init__, self, width = 0, height = 0, color = 'red', enfasis = 'strong' )

	def test_dentro_de_lista(self):

		lista = ('uno', 'dos', 'tres')
		self.assertIn('uno', lista, 'Uno debería estar en lista.')



class CalculadoraTest( unittest.TestCase ):

	def setUp(self):

		self.calc = Calculadora()
		# print( "Usos de PDB en tdd_func.py" )


	def test_calculadora_devuelve_suma_correcta(self):

		resultado = self.calc.sumar(2, 2)
		self.assertEqual( 4, resultado )


	def test_calculadora_devuelve_error(self):

		self.assertRaises( ValueError, self.calc.sumar, 'dos', 'tres')
		self.assertRaises( ValueError, self.calc.sumar, 2, 'tres')
		self.assertRaises( ValueError, self.calc.sumar, 'dos', 3 )


def suite_romanos():

	suite = unittest.TestSuite()
	resultado = unittest.TestResult()
	suite.addTest( unittest.makeSuite(RomanosTest) )
	runner = unittest.TextTestRunner()
	print( runner.run(suite) )

def suite_general():

	suite = unittest.TestSuite()
	resultado = unittest.TestResult()

	suite.addTest( unittest.makeSuite(RomanosTest) )
	suite.addTest( unittest.makeSuite(RectanguloTest) )
	suite.addTest( unittest.makeSuite(CalculadoraTest) )

	runner = unittest.TextTestRunner()
	runner.verbosity = 2
	print( "Suite General" )
	print( runner.run(suite) )



print( "Fin de programa" )

if __name__ == "__main__":

	assert a == 9, 'a no es 9'
	
	# unittest.main( verbosity = 2 )
	suite_general()
	# suite_romanos()

	'''
	unittest.main(
		module='__main__', 
		defaultTest = None,
		argv = None,
		testRunner = None,
		testLoader = unittest.defaultTestLoader,
		exit = True,
		verbosity = 1,		1/2/3
		failfast = None,	Stop on first fail or error
		catchbreak = None,	Catch ctrl-C and display results so far
		buffer = None,		Buffer stdout and stderr during tests
		warnings = None
	)

	-h, --help      show this help message and exit
	-v, --verbose   Verbose output
	-q, --quiet     Quiet output
	--locals        Show local variables in tracebacks
	-f, --failfast  Stop on first fail or error
	-c, --catch     Catch ctrl-C and display results so far
	-b, --buffer    Buffer stdout and stderr during tests
	'''



