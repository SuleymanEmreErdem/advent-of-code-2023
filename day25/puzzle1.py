import networkx as nx

file = open('input.txt', 'r')
rows = file.read().split('\n')
rows = [row.split(':') for row in rows]
rows = [[row[0], row[1].strip().split(' ')] for row in rows]

conns = set()
new_conns = []
min_cut = {}

for row in rows:
    for con in row[1]:
        conns.add(frozenset([row[0], con]))
for j in conns:
    new_conns.append(tuple(i for i in j))

G = nx.Graph()
G.add_edges_from((edge[0], edge[1], {'capacity': 1.0}) for edge in new_conns)

for i in new_conns:
    min_cut[i] = nx.minimum_cut_value(G, i[0], i[1])
min_cut = dict(sorted(min_cut.items(), key=lambda item: item[1]))
edges_to_cut = list(min_cut.keys())[:3]
print(edges_to_cut)
for edge in edges_to_cut:
    G.remove_edge(edge[0], edge[1])

res = 1

for comp in nx.connected_components(G):
    res *= len(comp)

print(res)