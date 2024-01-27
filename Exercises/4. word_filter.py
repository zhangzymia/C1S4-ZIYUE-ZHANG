import string
def word_filter_counter(text, filter_words):
    # Normalize the case of text and filter_words
    text = text.lower()
    filter_words = [word.lower() for word in filter_words]

    # Remove punctuation from text
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split text into words
    words = text.split()

    # Count occurrences of each filter word
    word_count = {word: words.count(word) for word in filter_words if word in words}

    return word_count

# Test cases
print(
    word_filter_counter("Hello world, hello!", ["hello"])
)  # Expected output: {'hello': 2}
print(
    word_filter_counter("The quick brown fox.", ["the"])
)  # Expected output: {'the': 1}
print(
    word_filter_counter(
        "Is this real life? Is this just fantasy?", ["is", "this", "just"]
    )
)  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(
    word_filter_counter(
        "Do we see the big picture or just small details?", ["we", "the", "or"]
    )
)  # Expected output: {'we': 1, 'the': 1, 'or': 1}
