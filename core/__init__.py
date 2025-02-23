# word_length_pathfinder/core/__init__.py
"""
Core functionality for text processing and graph building
Alapvető funkcionalitás szövegfeldolgozáshoz és gráfépítéshez
"""

from .text_processor import process_phrase, group_words_by_length
from .graph_builder import create_length_based_graph

__all__ = [
    'process_phrase',
    'group_words_by_length',
    'create_length_based_graph'
]