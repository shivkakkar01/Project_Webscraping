from collections import Counter
import re

def analyze_translated_headers(headers):
    """Find words repeated more than twice in headers."""
    words = re.findall(r'\w+', " ".join(headers).lower())
    word_count = Counter(words)
    repeated_words = {word: count for word, count in word_count.items() if count > 2}
    return repeated_words
