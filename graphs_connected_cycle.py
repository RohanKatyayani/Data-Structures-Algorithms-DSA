# Todo 1: Find all Connected Components in a Graph

from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u) # Undirected Graph

    def dfs(self, start, visited):
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def connected_components(self):
        visited = set()
        count = 0

        for node in range(self.V):
            if node not in visited:
                count +=1
                print(f"\nComponent {count}: ", end="")
                self.dfs(node, visited)

        print(f"\n\nTotal Connected Components: {count}")

    # Todo 2: Cycle Detection in Undirected Graph
    def is_cyclic_until(self, node, visited, parent):
        visited.add(node)
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                if self.is_cyclic_until(neighbour, visited, node):
                    return True
            elif neighbour != parent:
                return True
        return False

    def is_cyclic(self):
        visited = set()
        for node in range(self.V):
            if node not in visited:
                if self.is_cyclic_until(node, visited, -1):
                    return True
        return False

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 4)

    g.connected_components()

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(3, 4)

    if g.is_cyclic():
        print("\nCycle Detected")
    else:
        print("\nNo Cycle Detected")