#Todo: Path Reconstruction & Bellman-Ford Algorithm

import heapq
from collections import defaultdict

class WeightedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.nodes.add(u)
        self.nodes.add(v)

    def dijkstra(self, start):
        distance = {node: float('inf') for node in self.nodes}
        parent = {node: None for node in self.nodes}
        distance[start] = 0

        pq = [(0, start)]

        while pq:
            curr_dist, node = heapq.heappop(pq)

            if curr_dist > distance[node]:
                continue

            for neighbor, weight in self.graph[node]:
                new_dist = curr_dist + weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    parent[neighbor] = node
                    heapq.heappush(pq, (new_dist, neighbor))

        return distance, parent

    def reconstruct_path(self, parent, start, end):
        path = []
        while end is not None:
            path.append(end)
            end = parent[end]
        path.reverse()
        return path if path[0] == start else []

# Todo: Bellman-Ford Algorithm
class BellmanFord:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []  # (u, v, w)

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def bellman_ford(self, start):
        dist = {i: float('inf') for i in range(self.V)}
        dist[start] = 0

        # Step 1: Relax edges V-1 times
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 2: Check for negative cycles
        for u, v, w in self.edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("Graph contains a negative weight cycle!")
                return None

        return dist

if __name__ == "__main__":
    g = WeightedGraph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'E', 3)
    g.add_edge('E', 'D', 4)

    distances, parent = g.dijkstra('A')

    print("Shortest Distances from A:")
    print(distances)

    print("\nShortest Path from A to D:")
    print(g.reconstruct_path(parent, 'A', 'D'))

if __name__ == "__main__":
    bf = BellmanFord(5)
    bf.add_edge(0, 1, -1)
    bf.add_edge(0, 2, 4)
    bf.add_edge(1, 2, 3)
    bf.add_edge(1, 3, 2)
    bf.add_edge(1, 4, 2)
    bf.add_edge(3, 2, 5)
    bf.add_edge(3, 1, 1)
    bf.add_edge(4, 3, -3)

    print("Shortest distances from source (0):")
    print(bf.bellman_ford(0))