
import unittest
from sudoku import *

class TestTableroSudoku( unittest.TestCase ):

	def test_init(self):

		archivo = [
			"217385469", "385469712", "496721835",
			"524816973", "639547281", "871293546",
			"762158394", "953674128", "148932650",
		]

		resultado = [
			[2,1,7,3,8,5,4,6,9], [3,8,5,4,6,9,7,1,2,], [4,9,6,7,2,1,8,3,5],
			[5,2,4,8,1,6,9,7,3], [6,3,9,5,4,7,2,8,1,], [8,7,1,2,9,3,5,4,6],
			[7,6,2,1,5,8,3,9,4], [9,5,3,6,7,4,1,2,8,], [1,4,8,9,3,2,6,5,0],
		]

		
		self.assertEqual( resultado, TableroSudoku(archivo).tablero )
		self.assertEqual( resultado, _TableroSudoku__crear_tablero(archivo) )


	def test_init_ko(self):

		archivo = [
			"217385469", "385469712", "4967",
			"524816973", "639547281", "87129354",
			"762158394", "953674128", "14893",
		]

		self.assertRaises( SudokuError, TableroSudoku, archivo )




if __name__ == "__main__":


	unittest.main(
		verbosity = 2
	)
