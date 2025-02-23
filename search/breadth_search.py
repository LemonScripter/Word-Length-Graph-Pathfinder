# search/breadth_search.py
"""
Breadth-first search implementation
Szélességi keresés implementáció
"""

def breadth_first_search(graph, start_length, target_length):
    """Breadth-first search algorithm"""
    visited = set()
    queue = [(start_length, [start_length])]
    edges_traversed = 0
    
    while queue:
        current_length, path = queue.pop(0)
        if current_length not in visited:
            visited.add(current_length)
            edges_traversed += len(graph[current_length])
            
            if current_length == target_length:
                return path, len(visited), edges_traversed
            
            for neighbor in graph[current_length]:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))
    
    return [], 0, edges_traversed