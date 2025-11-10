def input_text():
    """
    Collect multiple lines of text input from the user.

    Returns:
        list: A list of strings entered by the user,
              stops collecting when empty line is entered.
    """
    sentences = []
    while True:
        sentence = input()
        if sentence == '':
            break
        sentences.append(sentence)
    return sentences


def clean_marks(text: str) -> str:
    """
    Remove punctuation marks from text and convert to lowercase.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: Cleaned text without punctuation marks in lowercase.
    """
    marks = [',', '.', '!', '?', ':', ';', '[', ']',
             '(', ')', '-', '"', '...', '(", ")']
    for mark in marks:
        text = text.replace(mark, '')
    return text.lower()


def count_words(sentences: list) -> tuple:
    """
    Count word occurrences in a list of sentences.

    Args:
        sentences (list): List of strings containing sentences.

    Returns:
        tuple: A tuple containing:
            - word_count (dict): Dictionary with words as keys and counts as values
            - repeated_words (list): List of words in order of first appearance
    """
    word_count = {}
    repeated_words = []

    for sentence in sentences:
        clean_sentence = clean_marks(sentence)
        words = clean_sentence.split()
        for word in words:
            if word not in word_count:
                word_count[word] = 0
                repeated_words.append(word)
            word_count[word] += 1
    return word_count, repeated_words


def sort_words(word_count: dict, repeated_words: list) -> None:
    """
    Sort and print words by frequency and order of appearance.

    Args:
        word_count (dict): Dictionary with words and their counts
        repeated_words (list): List of words in order of first appearance

    Returns:
        None: This function prints results directly
    """
    sorted_words = sorted(
        word_count.items(),
        key=lambda item: (-item[1], repeated_words.index(item[0]))
    )

    for word, count in sorted_words:
        print(word)


def main() -> None:
    """
    Main function to coordinate the word counting and sorting process.

    Returns:
        None
    """
    sentences = input_text()
    word_counts, word_order = count_words(sentences)
    sort_words(word_counts, word_order)


if __name__ == '__main__':
    main()
