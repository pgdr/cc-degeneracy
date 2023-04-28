import sys
import networkx as nx
from itertools import combinations as choose


def read_graph(csv_file):
    G = nx.Graph()

    with open(csv_file, "r", encoding="utf-8") as fin:
        for line in fin:
            u, v = map(int, line.split(","))
            G.add_edge(u, v)
    return G


def degeneracy_ordering(G):
    dgy = max(nx.core_number(G).values())
    cores = nx.core_number(G).items()
    ordered = sorted((k, v) for (v, k) in cores)
    # TODO verify that ordered is a degeneracy ordering!?  Should be 4?
    return dgy, [v for (_, v) in reversed(ordered)]


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


def common_neighbors(G, u, v):
    return set(nx.neighbors(G, u)).intersection(set(nx.neighbors(G, v)))


def c_closure(G):
    degeneracy, ordering = degeneracy_ordering(G)
    L = left_neighbors(G, ordering)
    # print(degeneracy)
    # print(ordering)
    C = 0  # the c-closure
    CW = None, None, []  # c-closure witness

    # for v in ordering:
    #     N_left = L[v]
    #     deg_left = len(N_left)
    #     print(v, deg_left, N_left)

    # print("CASE 1: u < v < x")
    for x in ordering:
        Nx = L[x]
        for u, v in choose(Nx, 2):
            if G.has_edge(u, v):
                continue
            Nuv = common_neighbors(G, u, v)
            if len(Nuv) > C:
                C = len(Nuv)
                CW = v, u, Nuv

    # print("CASE 2: u < x < v")
    for v in ordering:
        Nv = L[v]
        for x in Nv:
            Nx = L[x]
            for u in Nx:
                if G.has_edge(u, v):
                    continue
                Nuv = common_neighbors(G, u, v)
                if len(Nuv) > C:
                    C = len(Nuv)
                    CW = v, u, Nuv

    # print("CASE 3: x < u < v -> Note: only if c < degeneracy !")
    if C > degeneracy:
        return C, CW
    for v_idx, v in enumerate(ordering):
        Nv = L[v]
        for u_idx, u in enumerate(ordering):
            if u_idx >= v_idx:
                break
            if G.has_edge(u, v):
                continue
            Nu = L[u]
            Nuv = set(Nu).intersection(set(Nv))
            if len(Nuv) > C:
                C = len(Nuv)
                CW = v, u, Nuv
    return C, CW


def main():
    if len(sys.argv) != 2:
        exit("Usage: ccdeg arg")
    fname = sys.argv[1]
    graph = read_graph(fname)
    graph.remove_edges_from(nx.selfloop_edges(graph))
    print(c_closure(graph))


if __name__ == "__main__":
    main()
