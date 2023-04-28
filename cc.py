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


def common_neighbors(G, u, v):
    return set(nx.neighbors(G, u)).intersection(set(nx.neighbors(G, v)))


def c_closure(G):
    C = 0  # the c-closure
    CW = None, None, []  # c-closure witness
    for u, v in choose(G.nodes(), 2):
        if G.has_edge(u, v):
            continue
        Nuv = common_neighbors(G, u, v)
        if len(Nuv) > C:
            C = len(Nuv)
            CW = v, u, Nuv
    return C, CW


def main():
    if len(sys.argv) != 2:
        exit("Usage: cc arg")
    fname = sys.argv[1]
    graph = read_graph(fname)
    cc, cw = c_closure(graph)
    print(f"c-closure  = {cc}")


if __name__ == "__main__":
    main()
