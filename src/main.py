import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/network.csv")

# Create graph
G = nx.from_pandas_edgelist(df, 'source', 'target')

print("\n--- Basic Info ---")
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# -------------------------
# Centrality Measures
# -------------------------
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

print("\n--- Top Influential Nodes (Degree Centrality) ---")
top_nodes = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
for node, score in top_nodes:
    print(f"{node}: {score:.3f}")

# -------------------------
# Community Detection
# -------------------------
from networkx.algorithms import community

communities = list(community.greedy_modularity_communities(G))

print("\n--- Communities Detected ---")
for i, comm in enumerate(communities):
    print(f"Community {i+1}: {list(comm)}")

# -------------------------
# Visualization
# -------------------------
plt.figure(figsize=(8,6))
pos = nx.spring_layout(G, seed=42)

# Assign colors to communities
color_map = {}
for i, comm in enumerate(communities):
    for node in comm:
        color_map[node] = i

node_colors = [color_map[node] for node in G.nodes()]

nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=700)

plt.title("Social Network Graph with Communities")
plt.savefig("images/graph.png")
plt.show()
