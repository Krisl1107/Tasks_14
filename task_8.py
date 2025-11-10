def sort_string(user_str: str) -> str:
    """
    Sort characters in a string in ascending order.

    Args:
        user_string (str): The input string to be sorted

    Returns:
        str: A new string with characters sorted in ascending order

    """
    chars = list(user_str)
    chars.sort()
    sorted_chars = ''.join(chars)
    return sorted_chars


def main():
    """
    Main function to get user input and display sorted string.
    """
    user_str = input("Enter the string: ")
    sorted_str = sort_string(user_str)
    print("Sorted string:", sorted_str)


if __name__ == "__main__":
    main()
