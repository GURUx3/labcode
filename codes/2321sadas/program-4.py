def word_frequencies(text):
    """Count words in text without treating letter case as significant."""
    frequencies = {}
    for word in text.lower().split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


sentence = "Python is simple and Python is readable"
print(word_frequencies(sentence))
