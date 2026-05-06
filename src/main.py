import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# -------------------------
# Load Facebook dataset
# -------------------------
G = nx.read_edgelist("data/facebook.txt")

print("\n--- Basic Info ---")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# -------------------------
# Centrality Measures
# -------------------------
degree = nx.degree_centrality(G)
betweenness = nx.betweenness_centrality(G)

# Compare top nodes
top_degree = sorted(degree.items(), key=lambda x: x[1], reverse=True)[:5]
top_between = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop Degree Centrality Nodes:")
for n, v in top_degree:
    print(n, round(v, 4))

print("\nTop Betweenness Centrality Nodes:")
for n, v in top_between:
    print(n, round(v, 4))

# -------------------------
# Community Detection
# -------------------------
from networkx.algorithms import community

communities = list(community.greedy_modularity_communities(G))
print("\nCommunities Found:", len(communities))

# -------------------------
# Plotly Visualization
# -------------------------
pos = nx.spring_layout(G, seed=42)

edge_x = []
edge_y = []

for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5),
    hoverinfo='none',
    mode='lines'
)

node_x = []
node_y = []
node_text = []

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(f"Node {node}<br>Degree: {degree[node]:.4f}")

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    text=node_text,
    marker=dict(size=6)
)

fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title="Interactive Social Network Graph",
                    showlegend=False
                ))

fig.write_html("images/interactive_graph.html")
fig.show()
