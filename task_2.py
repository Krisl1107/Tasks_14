def check_input(elements: str) -> bool:
    """Validates user input according to specified criteria.

    Args:
        elements (list): List of strings to validate.

    Returns:
        bool: True if input is valid (contains exactly one '3' and all elements
              are integers), False otherwise.
    """
    if "3" not in elements:
        return False

    if elements.count("3") != 1:
        return False

    try:
        [int(el) for el in elements]
        return True
    except ValueError:
        return False


user_input = input("Enter integers separated by spaces. "
                   "The numbers must contain exactly one '3': ")
elements = user_input.strip().split()

if not check_input(elements):
    print("Invalid input, program terminated.")
    exit()

numbers = [int(el) for el in elements]
new_list = [el for el in numbers if el != 3]
print(new_list)
