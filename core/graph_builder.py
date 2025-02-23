# core/graph_builder.py
"""
Graph creation and management module
Gráf létrehozó és kezelő modul
"""
from collections import defaultdict

def create_length_based_graph(text):
    """Create a graph based on word and phrase lengths"""
    from .text_processor import group_words_by_length
    
    words = text.split()
    length_groups, length_counts, phrase_groups = group_words_by_length(text)
    graph = defaultdict(lambda: defaultdict(int))
    
    # Connect adjacent words
    for i in range(len(words) - 1):
        current_len = len(words[i])
        next_len = len(words[i + 1])
        if current_len != next_len:
            graph[current_len][next_len] += 1
            graph[next_len][current_len] += 1
    
    # Connect phrase lengths
    for i in range(len(words) - 1):
        for phrase_len in range(2, 6):
            if i + phrase_len <= len(words):
                phrase = ' '.join(words[i:i+phrase_len])
                phrase_len_total = len(phrase)
                if i + phrase_len < len(words):
                    next_word_len = len(words[i+phrase_len])
                    graph[phrase_len_total][next_word_len] += 1
                    graph[next_word_len][phrase_len_total] += 1
    
    return graph, length_groups, length_counts, phrase_groups