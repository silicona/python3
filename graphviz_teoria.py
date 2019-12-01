#!usr/bin/python3
# -*- coding: utf-8 -*-

'''
	Script pygraphviz - http://pygraphviz.github.io/

	Necesario tener instalado en local Graphviz

	Intalar paquete graphviz de Python - pip3 install graphviz



from graphviz import Digraph

dot = Digraph(comment = "La mesa redonda")

dot.node('A', "Rey Arturo")
dot.node('B', "Sir Lanceloto")
dot.node('E', "Lady Morgana")
dot.node('H', "Sir Hipopótamo")

dot.edges(['AB', 'BE', 'EH', 'AH'])
dot.edge('B', 'H', constraint = 'false')

print(dot.source)

'''


import pygraphviz as pgv

'''
Atributos de AGraph - http://www.graphviz.org/doc/info/attrs.html
strict - True  // strict graph (no parallel edges or self-loops).  
directed - False // [con strict = False] To create a digraph with possible parallel edges andself-loops use
landscape - False //
rank - Para subgraphs // source, same, min, max, sink 
ranksep - 0.1 // 
shape - http://www.graphviz.org/doc/info/shapes.html#polygon

'''

A = pgv.AGraph(penwidth = 3.0)

A.add_node('Solo')

A.add_edge(1,2)
A.add_edge(2,3)
A.add_edge(1, 3, color = 'green')

nodelist = ['B', 'C', 'D']
A.add_nodes_from(nodelist)

edgelist = [('B', 'C')]
A.add_edges_from(edgelist, color = 'grey')

cyclelist = ['H', 'J', 'K']
A.add_cycle(cyclelist)

A.graph_attr['label'] = "Label de Prueba"
A.node_attr['shape'] = 'circle'
A.edge_attr['color'] = 'red'

nodo = A.get_node('Solo')
nodo.attr['shape'] = 'box'

linea = A.get_edge(2,3)
linea.attr['color'] = 'blue'

Sub = A.add_subgraph([2, 'K', 'B'], name = 'Sub1', rank = "same", color = "red")
Sub.graph_attr['rank'] = 'same'



print(A.string()) # print to screen
print("Wrote simple.dot")
A.write('simple.dot') # write to simple.dot


B = pgv.AGraph('simple.dot') # create a new graph from file
B.layout() # layout with default (neato)
B.draw('simple.png') # draw png
print("Wrote simple.png")

dicty = {'1': {'2': None}, '2': {'1': None, '3': None}, '3': {'2': None}}
D = pgv.AGraph(dicty)
D.write("simple2.dot")
D.layout()
D.draw('simple2.png')

# Estrella - pulpular
est = pgv.AGraph()
# set some default node attributes
est.node_attr['style']='filled'
est.node_attr['shape']='circle'
est.node_attr['fixedsize']='true'
est.node_attr['fontcolor']='#FFFFFF'

# make a star in shades of red
for i in range(16):

	est.add_edge(0,i)
	n = est.get_node(i)
	n.attr['fillcolor'] = "#%2x0000"%(i*16)
	n.attr['height'] = "%s"%(i/16.0+0.5)
	n.attr['width'] = "%s"%(i/16.0+0.5)

est.layout()
est.draw('simple_estrella.png')

# Atributos

A = pgv.AGraph(directed=True,strict=True,rankdir='LR')
# add node 1 with color red
A.add_node(1,color='red') 
A.add_node(5,color='blue')
# add some edges
A.add_edge(1,2,color='green')
A.add_edge(2,3)
A.add_edge(1,3)
A.add_edge(3,4)
A.add_edge(3,5)
A.add_edge(3,6)
A.add_edge(4,6)
# adjust a graph parameter
A.graph_attr['epsilon']='0.001'
print(A.string()) # print dot file to standard output
A.layout('dot') # layout with dot
A.draw('simple_atributos.png') # write to file

A=pgv.AGraph()
# add some edges
A.add_edge(1,2)
A.add_edge(2,3)
A.add_edge(1,3)
A.add_edge(3,4)
A.add_edge(3,5)
A.add_edge(3,6)
A.add_edge(4,6)
# make a subgraph with rank='same'
B=A.add_subgraph([4,5,6],name='s1',rank='same')
B.graph_attr['rank']='same'
A.layout('dot') # layout with dot
A.draw('simple_sub.png') # write to file


# specify UTF-8 encoding (it is the default)
A=pgv.AGraph(encoding='UTF-8')

# nodes, attributes, etc can be strings or unicode
A.add_node(1,label='plain string')
A.add_node(2,label='unicode')

# you can enter unicode text as
hello='Здравствуйте!'
A.add_node(3,label=hello)

# or using unicode code points
hello='\u0417\u0434\u0440\u0430\u0432\u0441\u0442\u0432\u0443\u0439\u0442\u0435!'
A.add_node(hello) # unicode node label

goodbye="До свидания"
A.add_edge(1,hello,key=goodbye)

A.add_edge("שלום",hello)
#A.add_edge(1,3,hello="こんにちは / ｺﾝﾆﾁﾊ")
A.add_edge(1,"こんにちは")

print(A) # print to screen
# A.write('utf8.dot') # write to simple.dot
A.layout()
A.draw("simple_utf.png")

A = pgv.AGraph("html2.gv")
A.write('simple_html2.dot')
A.layout('dot')
A.draw('simple_html2.png')
