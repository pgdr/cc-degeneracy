from datetime import datetime as dt
import sys
import heapq


def _left_neighborhood(graph: list[list[int]], V_to_idx, v: int) -> list[int]:
    lv: list[int] = []
    for u in graph[v]:
        if V_to_idx[u] < V_to_idx[v]:
            lv.append(u)
    return lv


def left_neighbors(graph: list[list[int]], ordering: list[int]) -> dict[int, set[int]]:
    L = {}
    V_to_idx = {v: i for (i, v) in enumerate(ordering)}

    for v in range(len(graph)):
        L[v] = set(_left_neighborhood(graph, V_to_idx, v))
    return L


def has_edge(graph: list[list[int]], u: int, v: int) -> bool:
    if len(graph[u]) < len(graph[v]):
        v, u = u, v
    return u in graph[v]  # Can be done in O(d) time


def c_closure(graph, ordering, L) -> int:
    N = {v: set(graph[v]) for v in range(len(graph))}
    C = -2  # the c-closure

    #  CASE 1: u < v < x
    for x in ordering:
        Nx = list(L[x])
        for i_u in range(len(Nx)):
            u = Nx[i_u]
            for i_v in range(i_u + 1, len(Nx)):
                v = Nx[i_v]
                if has_edge(graph, u, v):
                    continue
                Nuv = N[u].intersection(N[v])
                if len(Nuv) > C:
                    C = len(Nuv)
    return C + 1


def degeneracy(graph: list[list[int]]) -> tuple[int, list[int]]:
    d = {v: len(graph[v]) for v in range(len(graph))}
    queue = [(d[v], v) for v in range(len(graph))]
    heapq.heapify(queue)
    retval: list[int] = []
    deg = 0
    while queue:
        dv, v = heapq.heappop(queue)
        if d[v] == -1:
            continue
        retval.append(v)
        for i in range(len(graph[v])):
            u = graph[v][i]
            if d[u] == -1:
                continue
            heapq.heappush(queue, (d[u] - 1, u))
        deg = max(deg, d[v])
        d[v] = -1
    return deg, list(reversed(retval))


def main() -> None:
    vertices: set[int] = set()
    edges: set[tuple[int, int]] = set()
    for line in sys.stdin:
        va, vb = line.split(" ")
        a = int(va)
        b = int(vb)
        vertices.add(a)
        vertices.add(b)
        edges.add((a, b))
    adj: list[list[int]] = [[] for _ in range(len(vertices) + 1)]
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    print(",", end="")
    print(len(adj), end=",")
    print(len(edges), end=",")
    del edges
    deg, ordering = degeneracy(adj)
    print(deg, end=",")
    L = left_neighbors(adj, ordering)
    start = dt.now()
    cc = c_closure(adj, ordering, L)
    end = dt.now()
    delta = round((end - start).total_seconds() * 1000, 1)

    print(f"{cc},{delta}")


main()
