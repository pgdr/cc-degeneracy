import sys
from itertools import combinations as choose
from datetime import datetime as dt
import heapq as Q
import networkx as nx


def read_graph(csv_file):
    G = nx.Graph()
    if csv_file.endswith(".gz"):
        import gzip

        with gzip.open(csv_file, "rt") as fin:
            for line in fin:
                u, v = map(int, line.split())
                G.add_edge(u, v)

    else:
        with open(csv_file, "r", encoding="utf-8") as fin:
            for line in fin:
                u, v = map(int, line.split(","))
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
        return C, CW
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
    return C, CW


def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: ccdeg dataset [dataset2, dataset3, ..., datasetn]")
    print("name,n,m,deg,c-c,time (ms),smaller")
    for fname in sys.argv[1:]:
        output = []
        output.append(f"`{fname}`")
        graph = read_graph(fname)
        graph.remove_edges_from(nx.selfloop_edges(graph))
        output.append(f"{len(graph.nodes())}")
        output.append(f"{len(graph.edges())}")
        dgy = max(nx.core_number(graph).values())
        output.append(f"{dgy}")
        start = dt.now()
        cc, _ = c_closure(graph)
        output.append(f"{cc}")
        end = dt.now()
        delta = round((end - start).total_seconds() * 1000, 1)
        output.append(f"{delta}")
        if cc < dgy:
            output.append('"**c !**"')
            output[0] = "*" + output[0]
        else:
            output.append("d")
        output[0] = f'"{output[0]}"'
        print(",".join(output))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
