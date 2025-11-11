holes_letters = ['a', 'b', 'd', 'e', 'g', 'o', 'p', 'q']


def count_letters(word: str) -> int:
    """
    Counts the number of letters in a word that have holes.

    Args:
        word (str): The word to analyze.

    Returns:
        int: The count of letters with holes in the word.
    """
    count = 0
    for ch in word:
        if ch in holes_letters:
            count += 1
    return count


def count_words(words: list) -> tuple:
    """
    Counts the total number of letters with and without holes in a list of words,
    and identifies words with two or more letters with holes.

    Args:
        words (list of str): The list of words to analyze.

    Returns:
        tuple:
            - letters_with_holes (int): Total count of letters with holes.
            - letters_without_holes (int): Total count of letters without holes.
            - words_with_holes (list of str): Words with two or more letters with holes.
    """
    letters_with_holes = 0
    letters_without_holes = 0
    words_with_holes = []

    for word in words:
        count_holes = count_letters(word)
        if count_holes >= 1:
            letters_with_holes += count_holes
            letters_without_holes += len(word) - count_holes
        else:
            letters_without_holes += len(word)

        if count_holes >= 2:
            words_with_holes.append(word)

    return letters_with_holes, letters_without_holes, words_with_holes


def main():
    """
    Main function to receive user input, process the words, and display statistics.
    """
    sentence = input("Enter a string: ").strip().lower()
    words = sentence.split()

    letters_with_holes, letters_without_holes, words_with_holes = count_words(words)

    print("Number of letters with holes:", letters_with_holes)
    print("Number of letters without holes:", letters_without_holes)
    print("Words with two or more letters with holes:", *words_with_holes)


if __name__ == "__main__":
    main()
