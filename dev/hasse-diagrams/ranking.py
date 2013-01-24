#!/usr/bin/python2

import pygraphviz as pgv
from dot2tex import dot2tex

G = pgv.AGraph()


G.node_attr['shape'] = 'rect'
G.edge_attr['arrowhead'] = 'normal'

condition_list = [ ('Align-R-Hd-Wd', '*mm'),
                   ('s-XM', 'Align-R-Hd-Wd'),
                   ('*mm', 'MaxLink-m-V'),
                   ('*mm', 'Parse-s'),
                   ('FtBin-m', '*mm'),
                   ('MaxLink-m-r', '*m-r'),
                   ('MaxLink-m-r', '*m-C'),
                   ('*m-C', '*m-V'),
                   ('*m-r', '*m-V'),
                   ('s-XM', 'Onset'),
                   ('Parse-s', '*ComplexOnset'),
                   ('*SharedMora', 'MaxLink-m-r'),
                   ('*SharedMora', 'MaxLink-m-C'),
                   ('*SharedMora', 'MaxLink-m-g'),
                   ('*SharedMora', 'MaxLink-m-gh'),
                   ('*SharedMora', 'MaxLink-m-oh'),
                   ('*SharedMora', 'MaxLink-m-xh'),
                   ('*SharedMora', 'MaxLink-m-ng'),
                   ('*ComplexOnset', '*SharedMora'),
                   ('Have-m-ng', '*m-ng'),
                   ('Have-m-ng', 'MaxLink-m-V'),
                   ('*m-dh', 'Have-m-dh'),
                   ('*m-dh', 'MaxLink-m-dh'),
                   ('*m-dh', 'MaxLink-m-C'),
                   ('*m-g', 'Have-m-g'),
                   ('*m-g', 'MaxLink-m-g'),
                   ('*m-g', 'MaxLink-m-C'),
                   ('Have-m-gh', '*m-gh'),
                   ('Have-m-gh', 'MaxLink-m-V'),
                   ('*m-oh', 'Have-m-oh'),
                   ('*m-oh', 'MaxLink-m-oh'),
                   ('*m-oh', 'MaxLink-m-C'),
                   ('*m-xh', 'Have-m-xh'),
                   ('*m-xh', 'MaxLink-m-xh'),
                   ('*m-xh', 'MaxLink-m-C'),
                   ('*LongSchwa', '*m-C'),
                   ('*LongSchwa', '*m-g'),
                   ('*LongSchwa', '*m-xh'),
                   ('*LongSchwa', '*m-oh'),
                   ('*LongSchwa', '*m-ng'),
                   ('MaxLink-m-r', 'Seg-XM'),
                   ('Have-m-gh', 'Seg-XM'),
                   ('Seg-XM', 'Have-m-oh'),
                   ('Seg-XM', '*m-V'),
                   ('Seg-XM', 'MaxLink-m-oh'),
# Let's have some fun
                   ('*m-gh', '*m-g'),
                   ('*m-g', '*m-oh'),
                   ('*m-oh', '*m-xh'),
                   ('*m-xh', '*m-dh'),
                   ('*m-dh', '*m-ng'),

                   ('*m-ng', '*m-r'),
                   ('*m-r', '*m-V'),
                   ('*m-C', '*m-V')
                   ]

for x, y in condition_list:
    G.add_edge(x, y)

G.layout(prog='dot')

s = G.string()

G.draw('ranking.png')

with open('tikz-code.tex', 'w') as f:
    f.write(dot2tex(s, format='tikz', straightedges=False, figonly=True))
