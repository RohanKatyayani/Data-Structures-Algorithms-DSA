# Todo 1: What is Graph?
"""
A Graph is a way to represent relationships or connections between things. Each graph has Vertices(Nodes) which are the
things themselves, and Edges, which are the connections between them.
Just like Google Maps, the Cities are Vertices and the Road between them is Edges.
"""

from collections import deque
# Todo 2: Graph Representation (Adjacency List):
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u) # Undirected

    def print_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node} -> {neighbors}")

    # Todo 3: BFS(Breadth First Search)
    """
    Explore nodes level-by-level (like waves). Use a queue to keep track of what to visit next.
    """
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    # Todo 4: DFS(Depth First Search)
    """
    Explore one branch deeply before backtracking. Can use recursion or a manual stack.
    """
    def dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.print_graph()

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)

    print("\nBFS Traversal:")
    g.bfs(0)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)

    print("\nDFS Traversal:")
    g.dfs(0)