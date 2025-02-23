# visualization/graph_viz.py
"""
Graph visualization functions
Gráf vizualizációs függvények
"""
import matplotlib.pyplot as plt
import networkx as nx

def visualize_phrase_graph(graph, phrase_groups, start_phrase, target_phrase, paths=None, ax=None):
    """Visualize the phrase-based graph with paths"""
    G = nx.Graph()
    
    # Add edges
    for node, edges in graph.items():
        for edge, weight in edges.items():
            G.add_edge(node, edge, weight=weight)
    
    # Create layout
    pos = nx.spring_layout(G)
    
    if ax is None:
        ax = plt.gca()
    
    # Draw graph
    nx.draw_networkx_edges(G, pos, alpha=0.2, ax=ax)
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', ax=ax)
    
    # Add labels
    labels = {node: f"{node}\n({len(phrase_groups.get(node, []))} phrases)"
              for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=8, ax=ax)
    
    # Highlight paths
    if paths:
        for path in paths:
            path_edges = list(zip(path[:-1], path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                                 edge_color='red', width=2, ax=ax)
    
    ax.set_title("Phrase Length Graph / Kifejezéshossz Gráf")
    ax.axis('off')