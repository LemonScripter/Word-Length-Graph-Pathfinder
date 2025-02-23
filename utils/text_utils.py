# utils/text_utils.py

import unicodedata

def strip_accents(text):
    """
    Remove accents from input string while properly handling Hungarian characters
    A bemeneti szövegből eltávolítja az ékezeteket, megfelelően kezelve a magyar karaktereket
    """
    normalized = unicodedata.normalize('NFKD', text)
    return ''.join(c for c in normalized if not unicodedata.combining(c))