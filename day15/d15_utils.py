import networkx as nx
import numpy as np


def load_data():
    """Read Day 15 puzzle input to numpy array."""
    with open("d15_input.txt") as f:
        data = f.read().splitlines()
    risk = np.array([list(line) for line in data], dtype=int)
    return risk


def get_lowest_risk(risk):
    """Get the lowest risk of any path from the top left to the bottom right."""
    # Create lattice graph
    G = nx.grid_2d_graph(risk.shape[0], risk.shape[1], create_using=nx.MultiDiGraph)

    # Add weights to edges
    for u, v, key in G.edges:
        G[u][v][key]["weight"] = risk[v]

    # Compute the path with lowest possible risk
    lowest_risk = nx.dijkstra_path_length(
        G, source=(0, 0), target=(risk.shape[0] - 1, risk.shape[1] - 1)
    )

    return lowest_risk
