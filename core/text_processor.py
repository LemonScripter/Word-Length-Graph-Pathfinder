# core/text_processor.py
"""
Text processing module for word length analysis
Szövegfeldolgozó modul szóhosszúság elemzéshez
"""
import string
from collections import defaultdict

def process_phrase(phrase):
    """Process a phrase and return its characteristics"""
    words = phrase.split()
    word_lengths = [len(word) for word in words]
    total_length = len(phrase)
    return total_length, word_lengths, words

def group_words_by_length(text):
    """Group words by their length and count occurrences"""
    words = [word.strip(string.punctuation) for word in text.split()]
    length_groups = defaultdict(set)
    length_counts = defaultdict(int)
    phrase_groups = defaultdict(list)
    
    # Single words
    for word in words:
        word_len = len(word)
        length_groups[word_len].add(word)
        length_counts[word_len] += 1
    
    # Phrases (2-5 words)
    for i in range(len(words)):
        for phrase_length in range(2, 6):
            if i + phrase_length <= len(words):
                phrase = ' '.join(words[i:i+phrase_length])
                total_length = len(phrase)
                phrase_groups[total_length].append(phrase)
    
    length_groups = {k: list(v) for k, v in length_groups.items()}
    return length_groups, length_counts, phrase_groups