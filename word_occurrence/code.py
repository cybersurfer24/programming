import re
from collections import defaultdict

def count_word_occurrences(text):
    word_counts = defaultdict(int)  

    words = re.findall(r'\b\w+\b', text.lower())  

    for word in words:
        word_counts[word] += 1

    return dict(word_counts)  

result = count_word_occurrences(text)
print(result)