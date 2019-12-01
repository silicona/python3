#!usr/bin/python3
# -*- coding: utf-8 -*-

'''
Script de esquema de relaciones de AyA
'''

import pygraphviz as pgv

import lib.funciones as Fx
import lib.templates_graphviz as Templates

G = pgv.AGraph(strict = True, directed = False, name = "dp_protocolo")

G.graph_attr['label'] = "Protocolo AyA"
G.graph_attr['labelloc'] = "t"
G.graph_attr['pad'] = .3

G.edge_attr['dir'] = 'forward'

lista_nodos = [
	'usuarios',
	'asociado',
	'llamada',
	'visita',
	'contacto',
	'propietario',
	'comprador',
	'operacion',
	'coordinador',
]

for nodo in lista_nodos:

	titulo_nodo = Templates.devuelve_template(nodo, True)
	G.add_node( nodo, label = '''<{}>'''.format(titulo_nodo) )

G.add_subgraph(['contacto', 'asociado'], name = "contacaso", rank = "same")

G.add_edge('llamada', 'visita')
G.add_edge('visita', 'contacto', style = "dashed")
G.add_edge('llamada', 'contacto')

# G.add_edge('asociado', 'contacto')
G.add_edge('comprador', 'operacion')
G.add_edge('contacto', 'asociado')
G.add_edge('asociado', 'comprador', label = "Comprador\ncon financiación")
G.add_edge('contacto', 'operacion', style = "dashed", label = "Comprador\nsin financiación", labelangle = -50.5)

G.add_edge('propietario', 'operacion', style = "dashed")



# print(G.to_string())
G.write('dp_prot.dot')

# G.layout()
G.layout('dot')
G.draw('dp_prot.png')