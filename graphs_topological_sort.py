# Todo: Topological Sorting & Cycle Detection (BFS – Kahn’s Algorithm)
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)  # Directed edge

    def topological_sort(self):
        indegree = [0] * self.V

        # Step 1: Calculate in-degree
        for u in self.graph:
            for v in self.graph[u]:
                indegree[v] += 1

        # Step 2: Initialize queue with nodes of indegree 0
        queue = deque([i for i in range(self.V) if indegree[i] == 0])
        topo_order = []

        # Step 3: Process queue
        while queue:
            node = queue.popleft()
            topo_order.append(node)

            # Reduce in-degree of neighbors
            for neighbor in self.graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all nodes are processed
        if len(topo_order) != self.V:
            print("Cycle detected! Topological sort not possible.")
        else:
            print("Topological Order:", topo_order)

if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    g.topological_sort()