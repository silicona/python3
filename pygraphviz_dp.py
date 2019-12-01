#!usr/bin/python3
# -*- coding: utf-8 -*-

'''
Script de esquema de relaciones de AyA
'''

import pygraphviz as pgv

import lib.funciones as Fx

lista_perfiles = [
	"admin",
	"financiero",
	"coordinador",
	"propietario",
	"comprador",
	"litigio",
]

# G = pgv.AGraph(strict = False, directed = True, name = "dp")
G = pgv.AGraph(name = "dp")

# G.graph_attr.update(
# 	strict = 'false'
# )
# G.graph_attr['directed'] = True
G.graph_attr['label'] = "Estructura de AyA"
G.graph_attr['labelloc'] = "t"
G.graph_attr['pad'] = .3
# G.graph_attr['size'] = 50
# G.graph_attr['ratio'] = .4
# G.graph_attr['epsilon'] = '0.11'
# G.graph_attr['center'] = True
# G.graph_attr['landscape'] = True
# G.graph_attr['splines'] = "ortho"
# G.graph_attr['quantum'] = 1.5
G.graph_attr['ranksep'] = .5
# G.graph_attr['nojustify'] = True

G.node_attr['shape'] = 'ellipse'
G.node_attr['style'] = 'filled'
G.node_attr['fillcolor'] = 'grey'
G.node_attr['pad'] = .5
G.node_attr['distorsion'] = -50.10
# G.node_attr['peripheries'] = 3
G.node_attr['pencolor'] = 'blue'

# G.edge_attr['color'] = 'red'
# G.edge_attr['arrowhead'] = 'halfopen'
# G.edge_attr['arrowtail'] = 'diamond'
G.edge_attr['dir'] = 'forward'
G.edge_attr['constraint'] = True


G.add_node('usuarios', shape = "cylinder")
G.add_node('asociados', shape = "cylinder")
G.add_node('contactos', shape = "cylinder")

cont = 0
for perfil in lista_perfiles:

	cont += 1

	label = Fx.poner_mayuscula(perfil)
	tabla_titulo = "".join([
		"<table border='0'>",
			"<tr>",
				"<td></td>",
				'<td port="titulo_arriba"></td>',
				"<td></td>",
			"</tr>",
			"<tr>",
				"<td colspan='3'>" + label + "</td>",
			"</tr>",
			"<tr>",
				"<td></td>",
				'<td port="titulo_abajo"></td>',
				"<td></td>",
			"</tr>",
		"</table>"
			
		])
	
	# G.add_node( perfil, shape = "record", sides = 5, label = '''{}'''.format(label) )
	# G.add_node( perfil, shape = "polygon", sides = 5, label = '''<{}>'''.format(tabla_titulo), ordering = "in" )
	G.add_node( perfil, shape = "polygon", sides = 5, label = '''<{}>'''.format(tabla_titulo), ordering = "out" )


G.add_node('llamadas', shape = "component")
G.add_node('visitas', shape = "component")

inicio_admin = "".join([
	'<table border="0">',
		'<tr>',
			'<td align="left" port="anuncio">Anuncios</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="gestion">Gestión comercial</td>',
		'</tr>',
		'<tr>',
			'<td align="left">Argumentario</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="">Consultas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="tecnico">&emsp;Técnico</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="comercial">&emsp;Comerciales</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="legal">&emsp;Legales</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="fiscal">&emsp;Fiscales</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="financiero">&emsp;Financieras</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="llamadas">Llamadas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="contactos">Contactos</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="visitas">Visitas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="ofertas">Ofertas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="propiedad">Propiedades</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="usuario">Usuarios</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="delegacion">Delegaciones</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="operacion">Operaciones</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="litigio">Litigios</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="publicidad">Volcados</td>',
		'</tr>',
	'</table>',
	])
G.add_node('inicio_admin', shape = "box", label = '''<%s>''' % inicio_admin)

inicio_coor = "".join([
	'<table border="0">',
		'<tr>',
			'<td align="left" port="anuncio">Anuncios</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="gestion">&emsp;Gestión comercial (Coordinador)</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="panel">&emsp;Panel de control (Delegado)</td>',
		'</tr>',
		'<tr>',
			'<td align="left">Argumentario</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="">Consultas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="tecnico">&emsp;Técnico</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="comercial">&emsp;Comerciales</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="legal">&emsp;Legales</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="fiscal">&emsp;Fiscales</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="financiero">&emsp;Financieras</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="llamadas">Llamadas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="contactos">Contactos</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="visitas">Visitas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="ofertas">Ofertas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="propiedad">Propiedades</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="usuario">Usuarios</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="operacion">Operaciones</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="litigio">Litigios</td>',
		'</tr>',
	'</table>',
	])
G.add_node('inicio_coor', shape = "box", label = '''<%s>''' % inicio_coor)

inicio_prop = "".join([
	'<table BORDER="0">',
		'<tr>',
			'<td ALIGN="LEFT">Panel de control</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="">Consultas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="comercial">&emsp;Comerciales</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="legal">&emsp;Legales</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="fiscal">&emsp;Fiscales</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="llamadas">Llamadas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="visitas">Visitas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="ofertas">Ofertas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="usuario">Mis datos</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="propiedad">Mi propiedad</td>',
		'</tr>',
	'</table>',
	])
G.add_node('inicio_prop', shape = "box", label = '''<%s>''' % inicio_prop)

inicio_comp = "".join([
	'<table BORDER="0">',
		'<tr>',
			'<td align="left" port="credito">Mi crédito</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="">Consultas</td>',
		'</tr><tr>',
			'<td align="left" port="legal">&emsp;Mi abogado</td>',
		'</tr><tr>',
			'<td align="left" port="fiscal">&emsp;Mi fiscal</td>',
		'</tr><tr>',
			'<td align="left" port="financiero">&emsp;Mi financiero</td>',
		'</tr><tr>',
			'<td align="left" port="usuario">Mis datos</td>',
		'</tr>',
	'</table>'
])
G.add_node('inicio_comp', shape = "box", label = '''<%s>''' % inicio_comp)

inicio_finan = "".join([
	'<table border="0" valign="top">',
		'<tr>',
			'<td align="left" port="">Consultas</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="legal">&emsp;Mi abogado</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="fiscal">&emsp;Mi fiscal</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="financiero">&emsp;Mi financiero</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="contacto">Contactos</td>',
		'</tr>',
		'<tr>',
			'<td align="left" port="operacion">Operaciones</td>',
		'</tr>',
	'</table>'
])
G.add_node('inicio_finan', shape = "box", label = '''<%s>''' % inicio_finan)


tabla_propiedad = "".join([
	'<table border="0" bgcolor="white">',
		'<tr>',
			'<td align="left" port="titulo">Propiedad:</td>',
		'</tr><tr>',
			'<td align="left" port="general">&emsp;General</td>',
		'</tr><tr>',
			'<td align="left" port="caracteristicas">&emsp;Características</td>',
		'</tr><tr>',
			'<td align="left" port="ubicacion">&emsp;Ubicación</td>',
		'</tr><tr>',
			'<td align="left" port="descripcion">&emsp;Descripción</td>',
		'</tr><tr>',
			'<td align="left" port="fotos">&emsp;Fotos</td>',
		'</tr><tr>',
			'<td align="left" port="publicidad">&emsp;Publicidad</td>',
		'</tr><tr>',
			'<td align="left" port="obs">&emsp;Observaciones</td>',
		'</tr><tr>',
			'<td align="left" port="docs">&emsp;Futuro Documentos</td>',
		'</tr>',
	'</table>',
	])
G.add_node('propiedad', shape = "record", label = '''<%s>''' % tabla_propiedad)

tabla_operacion = "".join([
	'<table border="0" bgcolor="white">',
		'<tr>',
			'<td align="left" port="titulo">Operación:</td>',
		'</tr><tr>',
			'<td align="left" port="general">&emsp;General</td>',
		'</tr><tr>',
			'<td align="left" port="comprador">&emsp;Compradores</td>',
		'</tr><tr>',
			'<td align="left" port="vendedor">&emsp;Vendedores</td>',
		'</tr><tr>',
			'<td align="left" port="propiedad">&emsp;Propiedad</td>',
		'</tr><tr>',
			'<td align="left" port="pre-venta">&emsp;Pre-Venta</td>',
		'</tr><tr>',
			'<td align="left" port="financiacion">&emsp;Financiación</td>',
		'</tr><tr>',
			'<td align="left" port="firma">&emsp;Firma</td>',
		'</tr><tr>',
			'<td align="left" port="facturacion">&emsp;Facturación</td>',
		'</tr><tr>',
			'<td align="left" port="docs">&emsp;Documentos</td>',
		'</tr>',
	'</table>',
	])
G.add_node('operacion', shape = "box", label = '''<%s>''' % tabla_operacion)

tabla_consultas = "".join([
	'<table border="0">',
		'<tr>',
		'<td align="left">Consultas:</td>',
		'</tr><tr>',
		'<td align="left" port="comercial">&emsp;Comerciales</td>',
		'</tr><tr>',
		'<td align="left" port="fiscal">&emsp;Fiscales</td>',
		'</tr><tr>',
		'<td align="left" port="financiero">&emsp;Financieras</td>',
		'</tr><tr>',
		'<td align="left" port="legal">&emsp;Juridicas</td>',
		'</tr><tr>',
		'<td align="left" port="tecnico">&emsp;Técnicas</td>',
		'</tr>',
	'</table>',
])
G.add_node('consultas', shape = "box", label = '''<%s>''' % tabla_consultas)


# sub_aso = G.add_subgraph(["asociados", "usuarios", "contactos"], name = "aso", rank = "same")
sub_usu = G.add_subgraph(lista_perfiles, name = "perfiles", rank = "same")
lista_inicios = [
	'inicio_admin',
	'inicio_coor',
	'inicio_prop',
	'inicio_comp',
	'inicio_finan'
]
# sub_ini = G.add_subgraph(lista_inicios, name = "inicios", rank = "same")
sub_sink = G.add_subgraph(['propiedad', 'consultas', 'operacion'], name = "inicios", rank = "max", ordering = "out")


G.add_edge("asociados", "usuarios")
# G.add_edge("usuarios", "asociados", dir = "none")
G.add_edge("asociados", "contactos")
# G.add_edge("Contactos", "Asociados" )

G.add_edge("contactos", "operacion", style = "dotted", headport = "comprador")
G.add_edge("contactos", "comprador" )

for perfil in lista_perfiles:

	G.add_edge("usuarios", perfil, headport = "titulo_arriba")


G.add_edge("llamadas", "visitas" )
G.add_edge("llamadas", "contactos" )
G.add_edge("visitas", "contactos", style = "dashed")

G.add_edge("admin", "inicio_admin")
G.add_edge("coordinador", "inicio_coor")
G.add_edge("propietario", "inicio_prop")
G.add_edge("comprador", "inicio_comp")
G.add_edge("financiero", "inicio_finan")
G.add_edge("inicio_finan", "operacion", tailport = "operacion", headport = "financiacion")

# G.add_edge("propietario", "propiedad")

# G.add_edge("comprador", "operacion")

# G.add_edge("inicio_coor", "consultas", tailport = "tecnico", headport = "tecnico")

# G.add_edge("inicio_prop", "consultas", tailport = "legal", headport = "legal")
G.add_edge("inicio_prop", "propiedad", tailport = "propiedad")

# G.add_edge("inicio_comp", "consultas", tailport = "legal", headport = "legal")
G.add_edge("inicio_comp", "operacion", tailport = "credito", headport = "financiacion")

# G.add_node('General', group = 'propiedad')
# G.add_node('Caracteristicas', label = "Características", group = 'propiedad')
# G.add_node('Fotos', group = 'propiedad')

# G.add_node('Comercial', group = 'soporte')
# G.add_node('Financiero', group = 'soporte')
# G.add_node('Fiscal', group = 'soporte')
# G.add_node('Juridico', group = 'soporte')
# G.add_node('Tecnico', group = 'soporte')

# lista_sop_prop = ["Comercial", "Financiero", "Juridico"]
# nodos_sop_prop = G.add_nodes_from(lista_sop_prop, group = "soporte", shape = 'polygon', sides = 7, regular = True)
# lista_sop_comp = ["Financiero_comp", "Fiscal", "Juridico_comp"]
# nodos_sop_comp = G.add_nodes_from(lista_sop_comp, group = "soporte_comp", shape = 'polygon', sides = 7)

# Sop = pgv.AGraph()
# Sop.add_nodes_from(["Comercial", "Financiero", "Fiscal", "Juridico"], group = "soporte")
# Sop.graph_attr['splines'] = False

# h = Sop.handle

# soporte_prop_attr = G.add_subgraph(Sop, name = "soporte_prop", rank = "same")

# sub_usu = G.add_subgraph(["inicio_prop", "propiedad", "inicio_comp", "operacion"], name = "herramientas", rank = "same")

# sub_aso.node_attr['peripheries'] = 1
# print(sub_aso)

# propiedad_attr = G.add_subgraph(["General", "Caracteristicas", "Fotos"], name = "propiedad", rank = "")
# sub_sop_prop = G.add_subgraph(lista_sop_prop, name = "soporte_prop", rank = "sink")
# sub_sop_comp = G.add_subgraph(lista_sop_comp, name = "soporte_comp", rank = "max")
# soporte_prop_attr.graph_attr['splines'] = False
# soporte_prop_attr.graph_attr['rank'] = "same"

# print(G.degree(lista_sop_prop, True))

# G.add_edge("Propiedad", "General", tailport = "here")

# G.add_edge("General", "Caracteristicas", dir = "none")
# G.add_edge("Caracteristicas", "Fotos", dir = "none")

# G.add_edge("Soporte_prop", "Comercial")
# G.add_edge("Comercial", "Financiero", dir = "none")
# # G.add_edge("Financiero", "Fiscal", dir = "none")
# G.add_edge("Financiero", "Juridico", dir = "none")

# G.add_edge("Soporte_comp", "Financiero_comp")
# # G.add_edge("Comercial", "Financiero", dir = "none")
# G.add_edge("Financiero_comp", "Fiscal", dir = "none")
# G.add_edge("Fiscal", "Juridico_comp", dir = "none")

# print(G.to_string())
G.write('graphviz_dp.dot')

# G.layout()
G.layout('dot')
G.draw('graphviz_dp.png')

