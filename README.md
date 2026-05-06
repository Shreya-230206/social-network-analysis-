# Social Network Analysis using Graph Analytics

## Overview
This project performs in-depth analysis of a real-world social network using graph theory and network science techniques. The goal is to identify **influential users**, understand **network structure**, and detect **community clusters**.

The analysis is performed on a Facebook social network dataset where:
- **Nodes** represent users
- **Edges** represent friendships/connections

---

## Objectives
- Model social network data as a graph
- Identify influential nodes using centrality measures
- Compare different influence metrics
- Detect communities within the network
- Build interactive visualizations for better interpretation
  
---

## Dataset
- Source: SNAP Facebook Dataset
- Format: Edge list (`node1 node2`)
- Type: Undirected graph

Example:
0 1
0 2
1 2

---

## Methodology

### 1. Graph Construction
The dataset is converted into a graph using NetworkX:
- Nodes → Users
- Edges → Connections

---

### 2. Centrality Analysis

#### Degree Centrality
- Measures how many direct connections a node has
- Indicates **popularity or activity level**

#### Betweenness Centrality
- Measures how often a node lies on shortest paths
- Indicates **control over information flow**

---

### Comparison: Degree vs Betweenness

| Metric | Meaning | Insight |
|-------|--------|--------|
| Degree Centrality | Number of connections | Highly connected users |
| Betweenness Centrality | Bridge nodes | Users connecting communities |

Key Insight:
- A node may have **low connections but high influence** if it connects clusters

---

### 3. Community Detection
- Algorithm: Greedy Modularity Optimization
- Groups nodes into clusters based on dense connections

Output:
- Multiple communities detected
- Each community represents a social group

---

### 4. Visualization

#### Static Graph
- Created using Matplotlib
- Shows overall structure

#### Interactive Graph
- Built using Plotly
- Features:
  - Hover to see node info
  - Zoom and pan
  - Explore connectivity dynamically

---

## Results & Insights

- Identified top influential nodes based on **degree centrality**
- Found bridge nodes using **betweenness centrality**
- Observed **clear community clusters**
- Nodes with high betweenness act as **connectors between groups**
- Network exhibits **clustered social behavior**, typical of real-world networks
  
---

## How to Run
1. Clone the repository:
``` bash
git clone https://github.com/Shreya-230206/social-network-analysis-
cd social-network-analysis
```
2. Install dependencies:
``` bash
pip install -r requirements.txt
```
3. Run the project:
``` bash
python src/main.py
```

## Output
- Console:
  - Top influential nodes
  - Community structure
- Files:
  - Interactive graph (`.html`)
  - Visual network representation
