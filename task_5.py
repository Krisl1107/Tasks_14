def calculate_average():
    """
    Calculates and displays the average of numbers entered by the user.
    Handles empty input and non-numeric values.
    """
    try:
        numbers = [int(num) for num in 
                   input("Please enter numbers separated by spaces: ").split()]
    except ValueError:
        print("Incorrect input, program terminated.")
        exit()

    if not numbers:
        print("There are no numbers to calculate the average.")
    else:
        average = sum(numbers) / len(numbers)
        print("average value:", average)


calculate_average()
