import sys
from itertools import combinations as choose
from datetime import datetime as dt
import heapq as Q
import networkx as nx
from networkx.algorithms import bipartite


def read_graph():
    G = nx.Graph()
    for line in sys.stdin:
        u, v = map(int, line.split())
        G.add_edge(u, v)
    return G


def degeneracy_ordering(G):
    degrees = {v: G.degree(v) for v in G.nodes()}
    pq = [(G.degree(v), v) for v in G.nodes()]
    Q.heapify(pq)
    ordering = []
    deg = 0
    while pq:
        _, v = Q.heappop(pq)
        if degrees[v] == -1:
            continue
        ordering.append(v)
        deg = max(deg, degrees[v])
        degrees[v] = -1
        for u in G.neighbors(v):
            if degrees[u] != -1:
                Q.heappush(pq, (degrees[u] - 1, u))
                degrees[u] -= 1
    return deg, list(reversed(ordering))


def _left_neighborhood(G, V_to_idx, v):
    Nv = nx.neighbors(G, v)
    for u in Nv:
        if V_to_idx[u] < V_to_idx[v]:
            yield u


def left_neighbors(G, ordering):
    L = {}
    V_to_idx = {v: i for (i, v) in enumerate(ordering)}

    for v in G.nodes():
        L[v] = set(_left_neighborhood(G, V_to_idx, v))
    return L


def c_closure(G):
    """the c-closure of a graph is the smallest integer such that any two
    non-adjacent vertices have less than common neighbors.

    10.1016/j.dam.2021.06.019

    We return the 1+size of largest common neighborhood u,v s.t. uv notin E
    """
    degeneracy, ordering = degeneracy_ordering(G)
    L = left_neighbors(G, ordering)
    N = {v: set(nx.neighbors(G, v)) for v in G.nodes()}
    C = 0  # the c-closure
    CW = None, None, []  # c-closure witness

    #  CASE 1: u < v < x
    for x in ordering:
        Nx = L[x]
        for u, v in choose(Nx, 2):
            if G.has_edge(u, v):
                continue
            Nuv = N[u].intersection(N[v])
            if len(Nuv) > C:
                C = len(Nuv)
                CW = v, u, Nuv

    # The next two cases only relevant when c < degeneracy
    if C >= degeneracy:
        return C + 1, CW
    #  CASE 2: u < x < v
    # Note, only when c < |Left(v)|
    for v in ordering:
        if C >= len(L[v]):
            continue
        for x in L[v]:
            for u in L[x]:
                if G.has_edge(u, v):
                    continue
                Nuv = L[v].intersection(N[u])
                if len(Nuv) > C:
                    # never happens?
                    C = len(Nuv)
                    CW = v, u, Nuv

    #  CASE 3: x < u < v
    # Note: only when c < min(|Left(u)|, |Left(v)|)
    for v_idx, v in enumerate(ordering):
        if len(L[v]) <= C:
            continue
        for u_idx, u in enumerate(ordering):
            if u_idx >= v_idx:
                break
            if G.has_edge(u, v):
                continue
            if len(L[u]) <= C:
                continue
            Nuv = L[u].intersection(L[v])
            if len(Nuv) > C:
                # never happens?
                C = len(Nuv)
                CW = v, u, Nuv
    return C + 1, CW


def main():
    output = []

    graph = read_graph()
    graph.remove_edges_from(nx.selfloop_edges(graph))
    output.append(f"{len(graph.nodes())}")
    output.append(f"{len(graph.edges())}")
    dgy = max(nx.core_number(graph).values())
    output.append(f"{dgy}")
    bip = bipartite.is_bipartite(graph)
    start = dt.now()
    cc, _ = c_closure(graph)
    end = dt.now()
    output.append(f"{cc}")
    delta = round((end - start).total_seconds() * 1000, 1)
    output.append(f"{delta}")
    if cc < dgy:
        output.append('"**c !**"')
    else:
        output.append("d")

    output.append("b" if bip else "u")

    print(",".join(output))


if __name__ == "__main__":
    main()
