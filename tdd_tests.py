#!usr/bin/python3
# -*- coding:utf-8 -*-
'''
Unit test for roman1.py - Convertido en tdd_func.py

This program is part of 'Dive Into Python 3', a free Python book for
experienced programmers.  Visit http://diveintopython3.org/ for the
latest version.
'''

import unittest
from tdd_func import *

class RomanosTest(unittest.TestCase):

	def setUp(self):

		self.romano = Romanos()

		self.valores_correctos = ( (1, 'I'),
			(2, 'II'),
			(3, 'III'),
			(4, 'IV'),
			(5, 'V'),
			(6, 'VI'),
			(7, 'VII'),
			(8, 'VIII'),
			(9, 'IX'),
			(10, 'X'),
			(50, 'L'),
			(100, 'C'),
			(500, 'D'),
			(1000, 'M'),
			(31, 'XXXI'),
			(148, 'CXLVIII'),
			(294, 'CCXCIV'),
			(312, 'CCCXII'),
			(421, 'CDXXI'),
			(528, 'DXXVIII'),
			(621, 'DCXXI'),
			(782, 'DCCLXXXII'),
			(870, 'DCCCLXX'),
			(941, 'CMXLI'),
			(1043, 'MXLIII'),
			(1110, 'MCX'),
			(1226, 'MCCXXVI'),
			(1301, 'MCCCI'),
			(1485, 'MCDLXXXV'),
			(1509, 'MDIX'),
			(1607, 'MDCVII'),
			(1754, 'MDCCLIV'),
			(1832, 'MDCCCXXXII'),
			(1993, 'MCMXCIII'),
			(2074, 'MMLXXIV'),
			(2152, 'MMCLII'),
			(2212, 'MMCCXII'),
			(2343, 'MMCCCXLIII'),
			(2499, 'MMCDXCIX'),
			(2574, 'MMDLXXIV'),
			(2646, 'MMDCXLVI'),
			(2723, 'MMDCCXXIII'),
			(2892, 'MMDCCCXCII'),
			(2975, 'MMCMLXXV'),
			(3051, 'MMMLI'),
			(3185, 'MMMCLXXXV'),
			(3250, 'MMMCCL'),
			(3313, 'MMMCCCXIII'),
			(3408, 'MMMCDVIII'),
			(3501, 'MMMDI'),
			(3610, 'MMMDCX'),
			(3743, 'MMMDCCXLIII'),
			(3844, 'MMMDCCCXLIV'),
			(3888, 'MMMDCCCLXXXVIII'),
			(3940, 'MMMCMXL'),
			(3999, 'MMMCMXCIX'),
			(4000, 'MMMM'),                                    
			# Añadido hasta 5000
			(4500, 'MMMMD'),
			(4888, 'MMMMDCCCLXXXVIII'),
			(4999, 'MMMMCMXCIX')
		)
	

	def test_a_romano_valores_correctos(self):

		'''a_romano deberia devolver un resultado conocido con una entrada conocida'''

		for entero, numeral in self.valores_correctos:

			resultado = self.romano.a_romano(entero)

			self.assertEqual(numeral, resultado, 'A_romano debería devolver el numeral' )


	def test_a_romano_entero_excesivo(self):

		'''a_romano debería devolver un error con un entero mayor o igual a 5000'''
		# self.assertRaises( ErrorFueraDeRango, self.romano.a_romano, 4000 )

		# Actualizacion a 5000
		self.assertRaises( ErrorFueraDeRango, self.romano.a_romano, 5000 )


	def test_a_romano_zero(self):

		'''a_romano debería fallar con 0'''
		self.assertRaises( ErrorFueraDeRango, self.romano.a_romano, 0 )    


	def test_a_romano_negativo(self):

		'''a_romano debería fallar con números negativos'''
		self.assertRaises( ErrorFueraDeRango, self.romano.a_romano, -1 )


	def test_a_romano_no_entero(self):

		'''a_romano debería fallar con números no enteros'''
		self.assertRaises( ErrorNoEntero, self.romano.a_romano, 0.5 )


	'''
	'''
	'''
		TEST DE DESDE ROMANO
	'''
	'''
	'''

	def test_desde_romano_valores_correctos(self):

		'''Desde_romano debería dar un resultado conocido a los valores conocidos'''
		for entero, numeral in self.valores_correctos:

			resultado = self.romano.desde_romano( numeral )

			self.assertEqual( entero, resultado, 'Desde_romano deberia devolver el entero' )


	def test_ida_vuelta(self):

		'''Desde_romano( a_romano(n) ) == n for all n'''

		# for entero in range(1,4000):
		for entero in range( 1, 5000 ):

			numeral = self.romano.a_romano( entero )

			resultado = self.romano.desde_romano( numeral )

			self.assertEqual( entero, resultado, 'El entero no es el mismo que al principio' )

	'''
	Ensure that the from_roman() function should fail when you pass it a string with too many repeated numerals. 
	How many is “too many” depends on the numeral. 
	'''
	def test_desde_romano_demasiados_numerales(self):

		'''from_roman should fail with too many repeated numerals'''
		# num_invalidos = ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII')
		num_invalidos = ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII')

		for num in num_invalidos:

			self.assertRaises( ErrorNumeralRomanoInvalido, self.romano.desde_romano, num )

	'''
	Check that certain patterns aren’t repeated.
	For example, IX is 9, but IXIX is never valid.
	'''
	def test_desde_romano_pares_repetidos(self):

		'''from_roman should fail with repeated pairs of numerals'''
		num_invalidos = ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV')

		for num in num_invalidos:

			self.assertRaises( ErrorNumeralRomanoInvalido, self.romano.desde_romano, num )

	'''
	Check that numerals appear in the correct order, from highest to lowest value.
	CL is 150, but LC is never valid, because the numeral for 50 can never come before the numeral for 100. 
	This test includes a randomly chosen set of invalid antecedents: I before M, V before X, and so on.
	'''
	def test_desde_romano_numeral_invalido(self):

		'''from_roman should fail with malformed antecedents'''
		num_invalidos = (
			'IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
			'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'
		)

		for num in num_invalidos:

			self.assertRaises( ErrorNumeralRomanoInvalido, self.romano.desde_romano, num )


	def test_desde_romano_entrada_vacia(self):

		'''from_roman should fail with blank string'''

		self.assertRaises( ErrorNumeralRomanoInvalido, self.romano.desde_romano, '' )

		