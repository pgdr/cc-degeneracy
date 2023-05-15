#include <algorithm>
#include <chrono>
#include <iostream>
#include <iterator>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using Set = std::unordered_set<int>;
using List = std::vector<int>;
using Map_i_i = std::unordered_map<int, int>;
using Map_i_s = std::unordered_map<int, Set>;
using Graph = std::vector<List>;
using Pair = std::pair<int, int>;

List degeneracy(Graph graph) {
  int n = graph.size();
  List ordering(n);
  List degree(n);
  std::vector<bool> visited(n, false);

  for (int u = 0; u < n; ++u) {
    degree[u] = graph[u].size();
  }

  std::priority_queue<Pair> pq;

  for (int u = 0; u < n; ++u) {
    pq.push(Pair({-degree[u], u}));
  }

  int idx = 0;

  while (!pq.empty()) {
    Pair dv_v = pq.top();
    pq.pop();
    int v = dv_v.second;

    if (visited[v])
      continue;

    ordering[idx++] = v;
    visited[v] = true;

    for (int u : graph[v]) {
      if (visited[u])
        continue;

      pq.push(Pair({-(--degree[u]), u}));
    }
  }

  std::reverse(ordering.begin(), ordering.end());
  return ordering;
}

List _left_neighborhood(const Graph &graph, const Map_i_i &V_to_idx, int v) {
  List lv;

  for (int u : graph[v]) {
    if (V_to_idx.at(u) < V_to_idx.at(v)) {
      lv.push_back(u);
    }
  }

  return lv;
}

Map_i_s left_neighbors(const Graph &graph, const List &ordering) {
  Map_i_s L;
  Map_i_i V_to_idx;

  for (int i = 0; i < ordering.size(); i++) {
    V_to_idx[ordering[i]] = i;
  }

  for (int v = 0; v < graph.size(); v++) {
    List lv = _left_neighborhood(graph, V_to_idx, v);
    L[v] = Set(lv.begin(), lv.end());
  }

  return L;
}

bool has_edge(const Graph &graph, int u, int v) {
  if (graph[u].size() < graph[v].size()) {
    int tmp = u;
    u = v;
    v = tmp;
  }

  return std::find(graph[v].begin(), graph[v].end(), u) != graph[v].end();
}


int c_closure(const Graph &graph,
              const List &ordering,
              const Map_i_s &L) {
  Map_i_s N;

  for (int v = 0; v < graph.size(); v++)
    N[v] = Set(graph[v].begin(), graph[v].end());

  int C = -2;  // the c-closure

  // CASE 1: u < v < x
  for (int x : ordering) {
    const List Nx ( L.at(x).begin(), L.at(x).end() );

    for (auto i_u = 0; i_u < Nx.size(); ++i_u) {
      auto u = Nx[i_u];

      for (auto i_v = i_u + 1; i_v < Nx.size(); ++i_v) {
        auto v = Nx[i_v];

        if (has_edge(graph, u, v))
          continue;

        Set Nuv;

        for (int w : N[u]) {
          if (N[v].count(w) > 0)
            Nuv.insert(w);
        }

        int size = Nuv.size();

        if (size > C)
          C = size;
      }
    }
  }

  return C + 1;
}

int main() {
  std::vector<Pair> edges;
  std::string line;

  while (std::getline(std::cin, line)) {
    List row;
    std::stringstream ss(line);
    std::string cell;

    while (std::getline(ss, cell, ' ')) {
      row.push_back(std::stoi(cell));
    }

    int a = row[0];
    int b = row[1];
    edges.push_back({a, b});
  }

  int m = edges.size();
  Graph graph;
  int maxVertex = 0;

  for (const auto &edge : edges) {
    maxVertex = std::max(maxVertex, std::max(edge.first, edge.second));
  }

  for (int i = 0; i < maxVertex + 1; i++)
    graph.push_back(List {});

  for (const auto &edge : edges) {
    int a = edge.first;
    int b = edge.second;
    graph[a].push_back(b);
    graph[b].push_back(a);
  }

  edges.clear();
  edges.shrink_to_fit();
  int n = graph.size();
  List ordering = degeneracy(graph);
  Map_i_s leftNeighbors = left_neighbors(graph, ordering);
  int deg = -1;

  for (int u = 0; u < graph.size(); ++u) {
    int size = leftNeighbors[u].size();

    if (size > deg)
      deg = size;
  }

  auto start_time = std::chrono::high_resolution_clock::now();
  int cClosure = c_closure(graph, ordering, leftNeighbors);
  auto end_time = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time);
  std::cout << n << "," << m << "," << deg << "," << cClosure << "," << duration.count() << ",";

  if (cClosure < deg)
    std::cout << "c";
  else
    std::cout << "d";

  std::cout << ",x" << std::endl;
  return 0;
}
