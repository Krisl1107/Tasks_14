def find_divisors(number: int) -> list:
    """
    Find all divisors of a given integer.

    Args:
        number (int): The integer for which to find divisors

    Returns:
        list: A list of all divisors including both positive and negative divisors
              for negative numbers, sorted in ascending order.
    """
    divisors = []

    for divisor in range(1, abs(number) + 1):
        if number % divisor == 0:
            divisors.append(divisor)

    if number < 0:
        divisors += [-divisor for divisor in divisors]

    return sorted(divisors)


def main():
    """
    Main function to get user input and display divisors.
    """
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Incorrect input, program terminated.")
        exit()

    divisors = find_divisors(number)
    print(divisors)


if __name__ == "__main__":
    main()
