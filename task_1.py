def check_input(elements: str) -> bool: 
    """Validates user input.

    Args:
        elements (list): List of strings to validate.

    Returns:
        bool: True if input is valid (exactly 10 integers), False otherwise.  
    """
    if len(elements) != 10:
        return False

    try:
        [int(el) for el in elements]
        return True
    except ValueError:
        return False


user_input = input("Enter 10 integers separated by spaces: ")
elements = user_input.strip().split()

if not check_input(elements):
    print("Invalid input, program terminated.")
    exit()

numbers = [int(el) for el in elements]
new_list = []
for num in range(8):
    new_list.append(numbers[num] + numbers[num + 1])
print(new_list)
