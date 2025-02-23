# search/optimized_search.py
"""
Optimized path search implementation
Optimalizált útvonalkereső implementáció
"""

def optimized_path_search(graph, length_counts, pos, target_length):
    """Optimized path search algorithm"""
    path = []
    visited = set()
    edge_count = 0
    start_node = max(length_counts.items(), key=lambda x: x[1])[0]
    current_node = start_node
    path.append(current_node)
    visited.add(current_node)
    edge_count += sum(graph[current_node].values())
    
    while current_node != target_length:
        if target_length in graph[current_node]:
            path.append(target_length)
            edge_count += graph[current_node][target_length]
            break
        
        neighbors = []
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                score = (0.4 * weight) + (0.6 * length_counts.get(neighbor, 0))
                neighbors.append((neighbor, score))
        
        if not neighbors:
            break
        
        next_node = max(neighbors, key=lambda x: x[1])[0]
        current_node = next_node
        path.append(current_node)
        visited.add(current_node)
        edge_count += sum(graph[current_node].values())
    
    return path