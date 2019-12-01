#!usr/bin/python3
# -*- coding: utf-8 -*-

'''
Script de esquema de relaciones de AyA
'''

import pygraphviz as pgv

import lib.funciones as Fx
import lib.templates_graphviz as Templates

lista_perfiles = [
	("admin", "inicio_admin", "central"),
	("legal", "inicio_legal", "central"),
	("fiscal", "inicio_legal", "central"),
	("financiero", "inicio_finan", "central"),
	("comercial", "inicio_comer", "asociados"),
	("coordinador", "inicio_dele", "asociados"),
	("delegado", "inicio_dele", "asociados"),
	("propietario", "inicio_prop", "asociados"),
	("comprador", "inicio_comp", "asociados"),
	("comer_finan", "inicio_comer_finan", "central"),
	("litigio", "inicio_liti", "central"),
]

# G = pgv.AGraph(strict = False, name = "dp")
G = pgv.AGraph(name = "dp")

G.graph_attr['label'] = "Perfiles de AyA"
G.graph_attr['labelloc'] = "t"
G.graph_attr['pad'] = .3

G.edge_attr['dir'] = 'forward'

titulo_usuarios = Templates.devuelve_template('usuarios', True)
G.add_node( 'usuarios', shape = "ellipse", label = '''<{}>'''.format(titulo_usuarios) )

titulo_central = Templates.devuelve_template('central', True)
G.add_node( 'central', shape = "ellipse", label = '''<{}>'''.format(titulo_central) )

titulo_asociados = Templates.devuelve_template('asociados', True)
G.add_node( 'asociados', shape = "ellipse", label = '''<{}>'''.format(titulo_asociados) )


cont = 0
perfiles = []
inicios = []
for perfil, inicio, origen in lista_perfiles:

	perfiles.append(perfil)
	inicios.append(inicio)

	tabla = Templates.devuelve_template(perfil, True)
	G.add_node( perfil, shape = "ellipse", group = "perfiles", label = '''<{}>'''.format(tabla), ordering = "out" )

	label_inicio = Templates.devuelve_template(inicio)
	G.add_node( inicio, shape = "box", group = inicio, label = '''<%s>''' % label_inicio )

	G.add_edge(perfil, inicio, tailport = "titulo_abajo")

	G.add_edge(origen, perfil)

	cont += 1

G.add_subgraph(['usuarios', 'central', 'asociados'], name = "origen", rank = "same")
G.add_subgraph(perfiles, name = "perfiles", rank = "same")
G.add_subgraph(inicios, name = "inicios", rank = "same")

G.add_edge("central", "usuarios", dir ="none")
G.add_edge("usuarios", "asociados", dir = "none")

G.add_edge("coordinador", "delegado", tailport = "titulo_abajo", headport = "titulo_abajo")

# Gestion de archivos
imagen = "".join([
	'<<table border="0">',
		'<tr>',
			'<td FIXEDSIZE="TRUE" WIDTH="20" HEIGHT="20"><img scale="BOTH" src="lib/img/save.png"/></td>',
			'<td>Gestión de archivos</td>',
		'</tr>',
		'<tr>',
			'<td align="left" colspan="2">Consultas - Multiple</td>'
		'</tr>',
		'<tr>',
			'<td align="left" colspan="2">Operaciones - Individual</td>'
		'</tr>',
		'<tr>',
			'<td align="left" colspan="2">Mi crédito - Individual</td>'
		'</tr>',
		'<tr>',
			'<td align="left" colspan="2">¿¿ Mi propiedad - Individual ??</td>'
		'</tr>',
	"</table>>"
])
G.add_node('comp_archivos', label = '''%s''' % imagen)

edges_archivos = [
	("inicio_legal", "comp_archivos"),
	("inicio_comp", "comp_archivos"),
	("inicio_prop", "comp_archivos"),
	("inicio_dele", "comp_archivos"),
	("inicio_finan", "comp_archivos"),
	("inicio_comer_finan", "comp_archivos"),
]
G.add_edges_from(edges_archivos, color = "green")


# print(G.to_string())
G.write('dp_perfiles.dot')

# G.layout()
G.layout('dot')
G.draw('dp_perfiles.png')

