#include <algorithm>
#include <chrono>
#include <iostream>
#include <iterator>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using List = std::vector<int>;
using Map_int_int = std::unordered_map<int, int>;
using Map_int_list = std::unordered_map<int, List>;
using Graph = std::vector<List>;
using Pair = std::pair<int, int>;

List degeneracy(const Graph &graph) {
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
  return std::move(ordering);
}

List _left_neighborhood(const Graph &graph, const Map_int_int &V_to_idx, int v) {
  List lv;

  for (int u : graph[v]) {
    if (V_to_idx.at(u) < V_to_idx.at(v)) {
      lv.push_back(u);
    }
  }

  return std::move(lv);
}

Map_int_list left_neighbors(const Graph &graph, const List &ordering) {
  Map_int_list L;
  Map_int_int V_to_idx;

  for (auto i = 0; i < ordering.size(); ++i) {
    V_to_idx[ordering[i]] = i;
  }

  for (int v = 0; v < graph.size(); v++) {
    L[v] = _left_neighborhood(graph, V_to_idx, v);
  }

  return std::move(L);
}

bool has_edge(const Graph &graph, int u, int v) {
  if (graph[u].size() > graph[v].size()) {
    int tmp = u;
    u = v;
    v = tmp;
  }

  return std::find(graph[v].begin(), graph[v].end(), u) != graph[v].end();
}


int c_closure(const Graph &graph,
              const List &ordering,
              const Map_int_list &L) {
  int C = -2;  // the c-closure

  // CASE 1: u < v < x
  for (int x : ordering) {
    for (auto i_u = 0; i_u < graph[x].size(); ++i_u) {
      auto u = graph[x][i_u];

      for (auto i_v = i_u + 1; i_v < graph[x].size(); ++i_v) {
        auto v = graph[x][i_v];

        if (((int)graph[u].size()) <= C || ((int)graph[v].size()) <= C)
          continue;

        if (has_edge(graph, u, v))
          continue;

        List Nuv;
        const List &small = (graph[u].size() < graph[v].size()) ? graph[u] : graph[v];
        const List &large = (graph[u].size() < graph[v].size()) ? graph[v] : graph[u];

        for (int e : small) {
          if (std::find(large.begin(), large.end(), e) != large.end())
            Nuv.push_back(e);
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
  Map_int_list leftNeighbors = left_neighbors(graph, ordering);
  int deg = -1;

  for (int u = 0; u < graph.size(); ++u) {
    int size = leftNeighbors[u].size();

    if (size > deg)
      deg = size;
  }

  //auto start_time = std::chrono::high_resolution_clock::now();
  int cClosure = c_closure(graph, ordering, leftNeighbors);
  //auto end_time = std::chrono::high_resolution_clock::now();
  //auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time);
  //std::cout << n << "," << m << "," << deg << "," << cClosure << "," << duration.count() << ",";
  //if (cClosure < deg)
  //  std::cout << "c";
  //else
  //  std::cout << "d";
  //std::cout << ",x" << std::endl;
  std::cout << cClosure << std::endl;
  return 0;
}
