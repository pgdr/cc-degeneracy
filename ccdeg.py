import sys
from itertools import combinations as choose
from datetime import datetime as dt
import heapq as Q
import networkx as nx


def read_graph(csv_file):
    G = nx.Graph()

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
        d, v = Q.heappop(pq)
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
    # print(degeneracy)
    # print(ordering)
    C = 0  # the c-closure
    CW = None, None, []  # c-closure witness

    # for v in ordering:
    #     N_left = L[v]
    #     deg_left = len(N_left)
    #     print(v, deg_left, N_left)

    # print("CASE 1: u < v < x")
    case1 = 0
    for x in ordering:
        Nx = L[x]
        for u, v in choose(Nx, 2):
            if G.has_edge(u, v):
                continue
            case1 += 1
            Nuv = N[u].intersection(N[v])
            if len(Nuv) > C:
                C = len(Nuv)
                CW = v, u, Nuv
    # print("...", case1, "\tc =", C)

    # print("CASE 2: u < x < v -> Note, only if c < Left(v)")
    if C < degeneracy:
        case2 = 0
        for v in ordering:
            Nv = L[v]
            if C >= len(Nv):
                continue
            for x in Nv:
                Nx = L[x]
                for u in Nx:
                    if G.has_edge(u, v):
                        continue
                    case2 += 1
                    Nuv = L[v].intersection(N[u])
                    if len(Nuv) > C:
                        C = len(Nuv)
                        CW = v, u, Nuv
    #    print("...", case2, "\tc =", C)

    # print("CASE 3: x < u < v -> Note: only if c < degeneracy !")
    case3 = 0
    if C < degeneracy:
        for v_idx, v in enumerate(ordering):
            Nv = L[v]
            if len(Nv) <= C:
                continue
            for u_idx, u in enumerate(ordering):
                if u_idx >= v_idx:
                    break
                if G.has_edge(u, v):
                    continue
                Nu = L[u]
                if len(Nu) <= C:
                    continue
                case3 += 1
                Nuv = Nu.intersection(Nv)
                if len(Nuv) > C:
                    C = len(Nuv)
                    CW = v, u, Nuv
    # print("...", case3, "\tc =", C)
    return C, CW


def main():
    if len(sys.argv) < 2:
        exit(
            "Usage: ccdeg dataset [dataset2, dataset3, ..., datasetn]"
        )
    print("name,n,m,deg,c-c,runtime,smaller")
    for fname in sys.argv[1:]:
        start = dt.now()
        # print(start)

        print(fname, end=",")

        graph = read_graph(fname)
        graph.remove_edges_from(nx.selfloop_edges(graph))
        print(f"{len(graph.nodes())}", end=",")
        print(f"{len(graph.edges())}", end=",")
        dgy = max(nx.core_number(graph).values())
        print(f"{dgy}", end=",")
        cc, cw = c_closure(graph)
        print(f"{cc}", end=",")
        # print(f"c-closure witness {cw[0], cw[1]}: \t {cw[2]}")
        end = dt.now()
        # print(end)
        delta = round((end - start).total_seconds() * 1000, 1)
        print(f"{delta}", end=",")
        print("c" if cc < dgy else "d")


if __name__ == "__main__":
    main()
