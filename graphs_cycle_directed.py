# Todo: Cycle Detection in Directed Graphs
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v) # Directed Edge

    def is_cyclic_until(self, node, visited, rec_stack):
        visited.add(node)
        rec_stack.add(node)
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                if self.is_cyclic_until(neighbour, visited, rec_stack):
                    return True
            elif neighbour in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    def is_cyclic(self):
        visited = set()
        rec_stack = set()

        for node in range(self.V):
            if node not in visited:
                if self.is_cyclic_until(node, visited, rec_stack):
                    return True
        return False

if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    # g.add_edge(2, 0)  # Creates a cycle (0 → 1 → 2 → 0)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    if g.is_cyclic():
        print("Cycle detected!")
    else:
        print("No cycle detected.")