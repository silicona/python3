# language: en
@etiqueta
Feature: Calculadora
	
	Como autor de este articulo
	Quiero demostrar
	Como escribir test con behave con el ejemplo de la calculadora

	Scenario: Sumar dos números

		Given Yo he introducido 2 en la calculadora

		And Yo tambien he introducido 7 en la calculadora

		When Yo presiono sumar

		Then la suma debe ser 9


	Scenario Outline: Sumar dos números cualquiera

		Given Yo he introducido <numero1> en la calculadora

		And Yo tambien he introducido <numero2> en la calculadora

		When Yo presiono sumar

		Then la suma debe ser <resultado>


		Examples:

			| numero1	| numero2	| resultado	|
			|	5		|	2		|	7		|
			|	4		|	8		|	12		|
			|	100		|	200		|	300		|