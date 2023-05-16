import sys
import networkx as nx


def read_graph():
    G = nx.Graph()
    print(f"Reading graph ...", file=sys.stderr)
    i = 0
    for line in sys.stdin:
        i+=1
        if line.startswith("#"):
            continue
        u, v = map(int, line.split())
        if i % 10000 == 0:
            print(f"n = {len(G.nodes())} ... (working)", file=sys.stderr)
        G.add_edge(u, v)
    print(f"done", file=sys.stderr)
    print(f"n = {len(G.nodes())}", file=sys.stderr)
    print(f"m = {len(G.edges())}", file=sys.stderr)
    return G


def main():
    G = read_graph()
    print(f"Removing self-loops", file=sys.stderr)
    G.remove_edges_from(nx.selfloop_edges(G))
    print(f"Normalizing", file=sys.stderr)
    G = nx.convert_node_labels_to_integers(G, first_label=0)
    print(f"Writing, n = {len(G.nodes())}, m = {len(G.edges())}", file=sys.stderr)

    for e in sorted(G.edges()):
        print(e[0], e[1])


if __name__ == "__main__":
    main()
