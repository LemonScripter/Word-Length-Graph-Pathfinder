# visualization/comparison_viz.py
"""
Search comparison visualization
Keresési összehasonlítás vizualizáció
"""
import matplotlib.pyplot as plt
import time
from search.optimized_search import optimized_path_search
from search.breadth_search import breadth_first_search

def compare_search_methods(graph, length_groups, length_counts, phrase_groups, pos, target_phrase):
    """Compare different search methods and return comparison data"""
    start_length = max(length_counts.items(), key=lambda x: x[1])[0]
    target_length = len(target_phrase)
    
    # Optimized search
    start_time = time.perf_counter()
    opt_path = optimized_path_search(graph, length_counts, pos, target_length)
    opt_time = time.perf_counter() - start_time
    opt_nodes = len(opt_path)
    opt_edges = sum(len(graph[node]) for node in opt_path)
    
    # Breadth-first search
    start_time = time.perf_counter()
    bfs_path, bfs_steps, bfs_edges = breadth_first_search(graph, start_length, target_length)
    bfs_time = time.perf_counter() - start_time
    bfs_nodes = len(bfs_path) if bfs_path else 0
    
    # Calculate differences
    time_diff_percent = ((opt_time - bfs_time) / bfs_time) * 100
    nodes_diff_percent = ((opt_nodes - bfs_nodes) / bfs_nodes) * 100
    edges_diff_percent = ((opt_edges - bfs_edges) / bfs_edges) * 100
    
    # Print comparison results
    print("\n=== Search Algorithm Comparison / Keresési algoritmusok összehasonlítása ===")
    print(f"Target phrase / Célkifejezés: {target_phrase} ({target_length} characters/karakter)")
    print(f"Starting point / Kezdőpont: {start_length} character words/karakteres szavak")
    
    print("\nOptimized search / Optimalizált keresés:")
    print(f" Runtime / Futási idő: {opt_time:.6f} seconds/másodperc")
    print(f" Nodes visited / Bejárt csomópontok: {opt_nodes}")
    print(f" Edges traversed / Bejárt élek: {opt_edges}")
    print(f" Path / Útvonal: {' -> '.join(map(str, opt_path))}")
    
    print("\nBreadth-first search / Szélességi keresés:")
    print(f" Runtime / Futási idő: {bfs_time:.6f} seconds/másodperc")
    print(f" Nodes visited / Bejárt csomópontok: {bfs_nodes}")
    print(f" Edges traversed / Bejárt élek: {bfs_edges}")
    if bfs_path:
        print(f" Path / Útvonal: {' -> '.join(map(str, bfs_path))}")
    else:
        print(" No path found! / Nem található út!")
    
    return {
        'opt_time': opt_time,
        'bfs_time': bfs_time,
        'opt_nodes': opt_nodes,
        'bfs_nodes': bfs_nodes,
        'opt_edges': opt_edges,
        'bfs_edges': bfs_edges,
        'opt_path': opt_path,
        'bfs_path': bfs_path
    }