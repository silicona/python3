#!usr/bin/python3
# -*- coding: utf-8 -*-

from behave import given, when, then
from ..tdd_func import Calculadora

@given('Yo he introducido {numero1:d} en la calculadora')

def poner_num1(contexto, num1):

	contexto.number1 = num1


@given('Yo tambien he introducido {numero2:d} en la calculadora')

def poner_num2(contexto, num2):

	contexto.numero2 = num2


@when('Yo presiono sumar')

def pulsar_sumar(contexto):

	contexto.calculadora = Calculadora()

	contexto.resultado = contexto.calculadora.sumar( contexto.number1, contexto.number2 )


@then('la suma debe ser {resultado:d}')

def comprobar_resultado(contexto, resultado):

	assert contexto.resultado == resultado