# utils/visualization.py
import matplotlib.pyplot as plt
import networkx as nx
from qiskit.visualization import plot_histogram, plot_state_city

def plot_results(counts):
    """Plots the measurement results of a quantum circuit execution."""
    plot_histogram(counts)
    plt.show()

def plot_density_matrix(state):
    """Visualizes a quantum state's density matrix."""
    plot_state_city(state, title='Density Matrix')
    plt.show()

def visualize_decoding_graph(nodes, edges):
    """Visualizes a decoding graph for quantum error correction."""
    graph = nx.Graph()
    for node in nodes:
        graph.add_node(node)
    for edge in edges:
        graph.add_edge(*edge)
    nx.draw(graph, with_labels=True, node_color='red', edge_color='blue')
    plt.show()