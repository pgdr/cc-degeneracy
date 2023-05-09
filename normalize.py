import sys
import networkx as nx


def read_graph():
    G = nx.Graph()
    for line in sys.stdin:
        u, v = map(int, line.split())
        G.add_edge(u, v)
    return G


def main():
    G = read_graph()
    G.remove_edges_from(nx.selfloop_edges(G))
    G = nx.convert_node_labels_to_integers(G, first_label=0)
    for e in sorted(G.edges()):
        print(e[0], e[1])


if __name__ == "__main__":
    main()
