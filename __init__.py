# word_length_pathfinder/__init__.py
"""
Word Length Graph Pathfinder
Szóhosszúság-alapú gráfkereső program
"""

from .core import process_phrase, group_words_by_length, create_length_based_graph
from .search import optimized_path_search, breadth_first_search
from .visualization import visualize_phrase_graph, compare_search_methods
from .utils import strip_accents

__version__ = '1.0.0'
__author__ = 'LemonScript | László SZŐKE | lemonscript.info'

# Make commonly used functions available at package level
__all__ = [
    'process_phrase',
    'group_words_by_length',
    'create_length_based_graph',
    'optimized_path_search',
    'breadth_first_search',
    'visualize_phrase_graph',
    'compare_search_methods',
    'strip_accents'
]