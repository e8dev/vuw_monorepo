import random

# Graph class
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []
        self.colors = {}

    def add_edge(self, u, v):
        self.edges.append((u, v))
        self.nodes.add(u)
        self.nodes.add(v)

    def number_of_edges(self):
        return len(self.edges)

    def set_node_color(self, node, color):
        self.colors[node] = color

    def get_node_color(self, node):
        return self.colors[node]

# Function to count the number of satisfied edges
def count_satisfied_edges(G):
    satisfied_edges = 0
    for u, v in G.edges:
        if G.get_node_color(u) != G.get_node_color(v):
            satisfied_edges += 1
    return satisfied_edges

# Las Vegas algorithm
def las_vegas_algo(G):
    max_satisfied_edges = G.number_of_edges()  # All edges satisfied
    threshold = (2 / 3) * max_satisfied_edges  # 2/3 of maximum satisfied edges
    colors = ['R', 'G', 'B']
    
    while True:
        # Randomly assign colors to each node
        for node in G.nodes:
            G.set_node_color(node, random.choice(colors))
        
        satisfied_edges = count_satisfied_edges(G)
        
        if satisfied_edges >= threshold:
            break
    
    return {node: G.get_node_color(node) for node in G.nodes}

# Initialize the graph and add edges
G = Graph()
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
for u, v in edges:
    G.add_edge(u, v)

# Run the Las Vegas 3-coloring algorithm
colors = las_vegas_algo(G)
print(f"Colors: {colors}")
print(f"Number of satisfied edges: {count_satisfied_edges(G)}")
