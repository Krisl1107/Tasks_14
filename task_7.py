def even_odd_sums(numbers: list) -> int:
    """
    Calculate sums of even and odd numbers in a list.

    Args:
        numbers (list): List of integers to process

    Returns:
        tuple: A tuple containing (sum_even, sum_odd) where:
            sum_even (int): Sum of all even numbers
            sum_odd (int): Sum of all odd numbers
    """
    sum_even = sum(num for num in numbers if num % 2 == 0)
    sum_odd = sum(numbers) - sum_even
    return sum_even, sum_odd


def user_numbers() -> list:
    """
    Get list of integers from user input.

    Returns:
        list: List of integers entered by user

    Raises:
        ValueError: If input contains non-integer values
    """
    input_string = input("Please enter numbers separated by spaces: ")
    numbers = [int(x) for x in input_string.split()]
    return numbers


def main():
    """
    Main function to get user input and display results.
    """
    try:
        numbers = user_numbers()
    except ValueError:
        print("Incorrect input, program terminated.")
        exit()

    sum_even, sum_odd = even_odd_sums(numbers)

    print("Sum of even: ", sum_even)
    print("Sum of odd: ", sum_odd)


if __name__ == "__main__":
    main()
