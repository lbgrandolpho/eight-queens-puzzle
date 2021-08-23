from igraph import *

adj = []
for i in range(64):
    adj.append([])
    for j in range(64):
        adj[i].append(0)

''' 
                Grafo representando tabuleiro de xadrez:
Cada casa do tabuleiro é um vértice e é conectado com todos as outras casas
presentes na mesma linha, mesma coluna, e mesmas diagonais.
'''

with open("grafo.txt", "r") as f:
    for l in f.readlines():
        i, j = l.strip().split()
        i = int(i)
        j = int(j)
        adj[i][j] = 1

g = Graph.Adjacency(adj, ADJ_UNDIRECTED)
layout = g.layout_grid()

'''
Pega-se agora o grafo complementar ao gerado.
'''

g = g.complementer(False)

global V, conj
V = list(range(64))
conj = []

'''
Usa-se algoritmo de Bron-Kerbosch para encontrar as cliques do grafo
complementar. Como as cliques de um grafo são os conjuntos independentes de seu
grafo complementar, as cliques aqui serão os conjuntos indepedentes do grafo
original.
'''

def bk(r, p, x):
    global V, conj
    if p == [] and x == []:
        conj = conj + [r]
        return

    for v in p[:]:
        t1 = r + [v]
        t2 = list(set(p) & set(g.neighbors(v)))
        t3 = list(set(x) & set(g.neighbors(v)))
        
        bk(t1, t2, t3)
        p.remove(v)
        x.append(v)

bk([], V, [])

rainhas = []
for i in conj:
    if len(i) == 8:
        rainhas.append(conj)

print("Soluções encontradas: "+str(len(rainhas)))