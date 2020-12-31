#!/usr/bin/python3

# https://github.com/nvictus/priority-queue-dictionary
# pip3 install pqdict

import argparse, sys, re
from pqdict import pqdict
inf = float("inf")

class Vertex:
    def __init__(self, name, parent=None, status='', priority=inf):
        self.name = name
        self.parent = parent
        self.status = status
        self.priority = priority
    def __str__(self):
        return '{}({})'.format(self.name, self.priority)

parser = argparse.ArgumentParser(
    description=u'BFS/DFS/PFS all in one',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-0', '--start', type=str, default='', 
    help='starting vertex')
parser.add_argument('-a', '--algo', type=str, default='', 
    help='type of algorithm, "bfs", "dfs", "prim", or "dijk"')
parser.add_argument('graph_file', help=u'graph definition')
args = parser.parse_args()

if not args.algo in ['bfs', 'dfs', 'prim', 'dijk']:
    print('must specify -a ...')
    sys.exit()
with open(args.graph_file, 'r') as f:
    lines = f.readlines()

n2v = {}    # dict to lookup vertex object using name as key
G = {}      # the graph as a dict of edge lists for vertices
isDirected = False
for li in lines:
    li = re.sub('#.*', '', li)
    if re.match('^\s*$', li):
        continue
    m = re.match('^%\s*(\w.*)', li)
    if m:
        m = m.group(1).split()
        if 'directed' in m:
            isDirected = True
        continue
    (uname, vname, weight) = re.match('^\s*(\w+)\s+(\w+)\s+(\d+)\s*$', li).group(1,2,3)
    if uname:
        if not uname in n2v: n2v[uname] = Vertex(uname)
        if not vname in n2v: n2v[vname] = Vertex(vname)
        if not uname in G: G[uname] = {}
        if not vname in G: G[vname] = {}
        G[uname][vname] = int(weight)
        if not isDirected: G[vname][uname] = G[uname][vname]
    else:
        print('warning: unmatched input skipped')


n2v = { vname: Vertex(vname) for vname in G.keys() }
fringe = pqdict(key=lambda v: v.priority)
if not args.start:
    args.start = sorted(list(n2v.keys()))[0]
n2v[args.start].priority = 0
fringe.additem(args.start, n2v[args.start])
vid = 0
while fringe:
    (undef, v) = fringe.popitem()
    v.status = 'visited'
    print(v, end=' ')
    p = v.parent
    while p:
        print(p, end=' ')
        p = p.parent
    print('')
    for wname in sorted(G[v.name].keys()):
        weight = G[v.name][wname]
        w = n2v[wname]
        if not w.status: vid += 1
        if args.algo == 'bfs':
            new_prio = vid
        elif args.algo == 'dfs':
            new_prio = -vid
        elif args.algo == 'prim':
            new_prio = weight
        elif args.algo == 'dijk':
            new_prio = v.priority + weight
        if not w.status:
            w.status = 'fringe'
            w.parent = v
            w.priority = new_prio
            fringe.additem(w.name, w)
        elif w.status == 'fringe' and not args.algo in ['dfs', 'bfs']:
            if new_prio < w.priority:
                w.parent = v
                w.priority = new_prio
                fringe.updateitem(w.name, w)
                fringe.heapify(w.name)

if args.algo == 'prim':
    total = 0
    for vname in G.keys():
        v = n2v[vname]
        if v.parent:
            total += G[vname][v.parent.name]
    print('MST total cost: {}'.format(total))

