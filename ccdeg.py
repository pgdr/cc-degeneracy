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

    print("CASE 1: u < v < x")
    case1 = 0
    for x in ordering:
        Nx = L[x]
        for u, v in choose(Nx, 2):
            if G.has_edge(u, v):
                continue
            case1 += 1
            Nuv = common_neighbors(G, u, v)
            if len(Nuv) > C:
                C = len(Nuv)
                CW = v, u, Nuv
    print("...", case1, "\tc =", C)

    print("CASE 2: u < x < v -> Note, only if c < Left(v)")
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
                Nuv = common_neighbors(G, u, v)
                if len(Nuv) > C:
                    C = len(Nuv)
                    CW = v, u, Nuv
    print("...", case2, "\tc =", C)

    print("CASE 3: x < u < v -> Note: only if c < degeneracy !")
    case3 = 0
    if C < degeneracy:
        for v_idx, v in enumerate(ordering):
            Nv = L[v]
            for u_idx, u in enumerate(ordering):
                if u_idx >= v_idx:
                    break
                if G.has_edge(u, v):
                    continue
                case3 += 1
                Nu = L[u]
                Nuv = set(Nu).intersection(set(Nv))
                if len(Nuv) > C:
                    C = len(Nuv)
                    CW = v, u, Nuv
    print("...", case3, "\tc =", C)
    return C, CW


def main():
    if len(sys.argv) != 2:
        exit("Usage: ccdeg arg")
    fname = sys.argv[1]
    graph = read_graph(fname)
    graph.remove_edges_from(nx.selfloop_edges(graph))
    dgy = max(nx.core_number(graph).values())
    cc, cw = c_closure(graph)
    print(f"degeneracy = {dgy}")
    print(f"c-closure  = {cc}")


if __name__ == "__main__":
    main()
