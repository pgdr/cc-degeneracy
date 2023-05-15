from datetime import datetime as dt
import sys
import heapq
import signal


def _left_neighborhood(
    graph: list[list[int]], V_to_idx: dict[int, int], v: int
) -> list[int]:
    lv: list[int] = []
    for u in graph[v]:
        if V_to_idx[u] < V_to_idx[v]:
            lv.append(u)
    return lv


def left_neighbors(
    graph: list[list[int]], ordering: list[int]
) -> dict[int, set[int]]:
    L = {}
    V_to_idx = {v: i for (i, v) in enumerate(ordering)}

    for v in range(len(graph)):
        L[v] = set(_left_neighborhood(graph, V_to_idx, v))
    return L, V_to_idx


def has_edge(graph, L, V_to_idx, u: int, v: int) -> bool:
    if V_to_idx[v] > V_to_idx[u]:
        return u in L[v]
    return v in L[u]


def c_closure(graph, ordering, L, V_to_idx, dgy) -> int:
    N = {v: set(graph[v]) for v in range(len(graph))}
    C = -2  # the c-closure

    #  CASE 1: u < v < x
    for x in ordering:
        Nx = list(L[x])
        for i_u in range(len(Nx)):
            u = Nx[i_u]
            for i_v in range(i_u + 1, len(Nx)):
                v = Nx[i_v]
                if len(N[u]) <= C or len(N[v]) <= C:
                    continue
                if has_edge(graph, L, V_to_idx, u, v):
                    continue
                Nuv = N[u].intersection(N[v])
                if len(Nuv) > C:
                    C = len(Nuv)

    # The next two cases only relevant when c < degeneracy
    if C >= dgy:
        return C + 1

    #  CASE 2: u < x < v
    # Note, only when c < |Left(v)|
    for v in ordering:
        if C >= len(L[v]):
            continue
        for x in L[v]:
            for u in L[x]:
                if has_edge(graph, L, V_to_idx, u, v):
                    continue
                Nuv = L[v].intersection(N[u])
                if len(Nuv) > C:
                    C = len(Nuv)

    #  CASE 3: x < u < v
    # Note: only when c < min(|Left(u)|, |Left(v)|)
    for v_idx, v in enumerate(ordering):
        if len(L[v]) <= C:
            continue
        for u_idx, u in enumerate(ordering):
            if u_idx >= v_idx:
                break
            if has_edge(graph, L, V_to_idx, u, v):
                continue
            if len(L[u]) <= C:
                continue
            Nuv = L[u].intersection(L[v])
            if len(Nuv) > C:
                C = len(Nuv)

    return C + 1


def degeneracy(graph: list[list[int]]) -> tuple[int, list[int]]:
    d = {v: len(graph[v]) for v in range(len(graph))}
    queue = [(d[v], v) for v in range(len(graph))]
    heapq.heapify(queue)
    ordering: list[int] = []
    deg = 0
    while queue:
        _, v = heapq.heappop(queue)
        if d[v] == -1:
            continue
        ordering.append(v)
        deg = max(deg, d[v])
        d[v] = -1
        for i in range(len(graph[v])):
            u = graph[v][i]
            if d[u] == -1:
                continue
            heapq.heappush(queue, (d[u] - 1, u))
            d[u] -= 1
    return deg, list(reversed(ordering))


output = []


def kill(signal, frame, message="killed"):
    global output
    output.append(message)
    print(",".join(output))
    sys.stdout.flush()
    sys.exit(4)


def main() -> None:
    global output
    signal.signal(signal.SIGTERM, kill)
    vertices: set[int] = set()
    edges: set[tuple[int, int]] = set()

    try:
        N = 0
        for line in sys.stdin:
            va, vb = line.split()
            a = int(va)
            b = int(vb)
            N = max((a, b, N))
            vertices.add(a)
            vertices.add(b)
            edges.add((a, b))
        adj: list[list[int]] = [[] for _ in range(len(vertices) + 1)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
    except Exception as err:
        kill(0, 0, str(err))

    output.append(str(N + 1))
    output.append(str(len(edges)))
    del edges
    dgy, ordering = degeneracy(adj)
    output.append(str(dgy))
    L, V_to_idx = left_neighbors(adj, ordering)
    start = dt.now()
    cc = c_closure(adj, ordering, L, V_to_idx, dgy)
    end = dt.now()
    delta = round((end - start).total_seconds() * 1000, 1)
    output.append(str(cc))
    output.append(str(delta))
    output.append("c" if cc < dgy else "d")
    output.append("x")
    print(",".join(output))


if __name__ == "__main__":
    main()
