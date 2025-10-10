# Todo: Shortest Path Algorithms (Unweighted & Weighted Graphs)

# Todo 1: Shortest Path in Unweighted Graph (BFS)
from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def shortest_path(self, start):
        distance = {node: float('inf') for node in self.graph}
        distance[start] = 0

        queue = deque([start])

        while queue:
            node = queue.popleft()

            for neighbour in self.graph[node]:
                if distance[neighbour] == float('inf'):
                    distance[neighbour] = distance[node] + 1
                    queue.append(neighbour)

        return distance

# Todo 2: Shortest Path in Weighted Graph (Dijkstra’s Algorithm)
import heapq

class WeightedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()  # Keep track of all unique nodes

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))  # Directed weighted edge
        self.nodes.add(u)
        self.nodes.add(v)

    def dijkstra(self, start):
        # Initialize distances for all nodes (including destinations)
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        pq = [(0, start)]  # (distance, node)

        while pq:
            curr_dist, node = heapq.heappop(pq)

            if curr_dist > distances[node]:
                continue  # Skip outdated entries

            for neighbor, weight in self.graph[node]:
                new_dist = curr_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return distances

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)

    print("Shortest distances from node 0:")
    print(g.shortest_path(0))

if __name__ == "__main__":
    wg = WeightedGraph()
    wg.add_edge('A', 'B', 4)
    wg.add_edge('A', 'C', 2)
    wg.add_edge('B', 'C', 5)
    wg.add_edge('B', 'D', 10)
    wg.add_edge('C', 'E', 3)
    wg.add_edge('E', 'D', 4)

    print("Shortest distances from node A:")
    print(wg.dijkstra('A'))