# Readme BDD Python3

Suite de Test por BDD con 'Behave'

Instalar con pip behave. Crear carpeta propia
Modulos necesarios:
behave
faker
splinter (incluye selenium)
config

[Documentacion Github](https://github.com/behave/behave)

## Lenguaje Gherkin

Palabras clave:
	: Feature
	: Scenario
	: Scenario Outline
	: Background:
	: Examples

Palabras de pasos:
	: Given
	: When
	: Then
	: And

### Ejecución de Tests

Pasos para crear tests:
	: Creacion de bdd/calculadora.feature con sus escenarios propios
	: Creacion de Carpeta steps y el archivo step_definition.py de cada feature
	: Ejecutar `behave <nombre_archivo>`