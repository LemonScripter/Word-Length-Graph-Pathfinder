# main.py
"""
Main program entry point
Főprogram belépési pont
"""
import matplotlib.pyplot as plt
import networkx as nx
from core.text_processor import process_phrase
from core.graph_builder import create_length_based_graph
from visualization.graph_viz import visualize_phrase_graph
from visualization.comparison_viz import compare_search_methods
from utils.text_utils import strip_accents

def main(text, target_phrase):
    """Main function to analyze text and find paths to target phrase"""
    print(f"\n=== Analyzing text for target phrase: '{target_phrase}' ===")
    print(f"=== Szöveg elemzése a következő célkifejezéshez: '{target_phrase}' ===\n")
    
    # Create graph
    graph, length_groups, length_counts, phrase_groups = create_length_based_graph(text)
    
    # Find phrase characteristics
    target_len = len(target_phrase)
    target_info = process_phrase(target_phrase)
    
    print(f"Target phrase length: {target_len} characters")
    print(f"Célkifejezés hossza: {target_len} karakter")
    print(f"Individual word lengths: {target_info[1]}")
    print(f"Szavak egyedi hosszai: {target_info[1]}\n")
    
    # Find phrase occurrences
    words = text.split()
    target_words = target_phrase.split()
    seen_positions = set()
    occurrences = []
    
    for i in range(len(words) - len(target_words) + 1):
        current_words = words[i:i+len(target_words)]
        
        # Check words individually for matches
        match = True
        for curr_word, target_word in zip(current_words, target_words):
            curr_stripped = strip_accents(curr_word.lower())
            target_stripped = strip_accents(target_word.lower())
            
            # Compare first 4 characters (or whole word if shorter)
            min_length = min(4, len(curr_stripped), len(target_stripped))
            if not curr_stripped.startswith(target_stripped[:min_length]):
                match = False
                break
        
        if match:
            text_pos = i
            if text_pos not in seen_positions:
                seen_positions.add(text_pos)
                before_context = ' '.join(words[max(0, i-3):i])
                after_context = ' '.join(words[i+len(target_words):i+len(target_words)+3])
                occurrences.append({
                    'text_position': text_pos,
                    'word_position': i + 1,
                    'context': f"...{before_context} **{' '.join(words[i:i+len(target_words)])}** {after_context}..."
                })
    
    if occurrences:
        print(f"FOUND: The phrase '{target_phrase}' (and its variants) appears {len(occurrences)} time(s) in the text!")
        print(f"TALÁLAT: A '{target_phrase}' kifejezés (és ragozott alakjai) {len(occurrences)}x fordul elő a szövegben!")
        for i, occ in enumerate(occurrences, 1):
            print(f"\nOccurrence {i} (at word position {occ['word_position']}):")
            print(f"{i}. előfordulás (a {occ['word_position']}. szónál):")
            print(f"Context/Kontextus: {occ['context']}")
    else:
        print(f"NOT FOUND: The phrase '{target_phrase}' (or its variants) does not exist in the text!")
        print(f"NINCS TALÁLAT: A '{target_phrase}' kifejezés (vagy ragozott alakjai) nem található a szövegben!")

    # Compare search methods and visualize results
    try:
        # Create graph layout
        G = nx.Graph()
        for node, edges in graph.items():
            for edge in edges:
                G.add_edge(node, edge)
        pos = nx.spring_layout(G)
        
        # Get comparison data
        comparison_data = compare_search_methods(
            graph, length_groups, length_counts, phrase_groups, pos, target_phrase
        )
        
        # Create figures for visualization
        fig1, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
        
        # Runtime comparison
        ax1.bar(['Optimized\nOptimalizált', 'BFS\nSzélességi'],
                [comparison_data['opt_time'], comparison_data['bfs_time']])
        ax1.set_title('Runtime Comparison\nFutási idő összehasonlítás')
        ax1.set_ylabel('Time (s) / Idő (mp)')
        
        # Nodes comparison
        ax2.bar(['Optimized\nOptimalizált', 'BFS\nSzélességi'],
                [comparison_data['opt_nodes'], comparison_data['bfs_nodes']])
        ax2.set_title('Nodes Visited\nBejárt csomópontok')
        ax2.set_ylabel('Number of nodes\nCsomópontok száma')
        
        # Edges comparison
        ax3.bar(['Optimized\nOptimalizált', 'BFS\nSzélességi'],
                [comparison_data['opt_edges'], comparison_data['bfs_edges']])
        ax3.set_title('Edges Traversed\nBejárt élek')
        ax3.set_ylabel('Number of edges\nÉlek száma')
        
        plt.tight_layout()
        plt.show()

        # Create figure for phrase graph
        fig2, ax4 = plt.subplots(figsize=(12, 8))
        visualize_phrase_graph(graph, phrase_groups, None, target_phrase,
                             [comparison_data['opt_path']], ax4)
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Error during visualization / Hiba történt a megjelenítés során: {str(e)}")

if __name__ == "__main__":
    try:
        print("Program indítása...")
        # Read text from file
        with open('sample/input_text.txt', 'r', encoding='utf-8') as file:
            input_text = file.read().strip()  # Remove extra spaces and newlines
        main(input_text, "olvashat")
        print("Program sikeresen lefutott.")
    except FileNotFoundError:
        print("Hiba: Az input_text.txt fájl nem található a sample könyvtárban!")
    except Exception as e:
        print(f"Hiba történt: {str(e)}")