"""
This script computes basic statistics (mean, median, mode, variance, and standard deviation)
from a file containing numeric data. It also measures the time taken to process the data
and outputs the results to the console and to a file named 'StatisticsResults.txt'.
"""

import sys
import time


def calculate_mean(numbers):
    """
    Calculates the mean (average) of the given list of numbers.

    Args:
        numbers (list): A list of numerical values.

    Returns:
        float: The mean of the numbers, rounded to 2 decimal places.
    """
    total = sum(numbers)
    return round(total / len(numbers), 2) if numbers else 0


def calculate_median(numbers):
    """
    Calculates the median of the given list of numbers.

    Args:
        numbers (list): A list of numerical values.

    Returns:
        float: The median of the numbers, rounded to 2 decimal places.
    """
    numbers.sort()
    n = len(numbers)
    middle = n // 2
    if n % 2 == 0:
        return round((numbers[middle - 1] + numbers[middle]) / 2, 2)
    return round(numbers[middle], 2)


def calculate_mode(numbers):
    """
    Calculates the mode of the given list of numbers.

    Args:
        numbers (list): A list of numerical values.

    Returns:
        list: A list of the modes, rounded to 2 decimal places.
    """
    frequency = {}
    max_count = 0
    mode = []

    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
        max_count = max(max_count, frequency[num])

    for num, count in frequency.items():
        if count == max_count:
            mode.append(round(num, 2))

    return mode


def calculate_variance(numbers, mean):
    """
    Calculates the variance of the given list of numbers.

    Args:
        numbers (list): A list of numerical values.
        mean (float): The mean of the numbers.

    Returns:
        float: The variance of the numbers, rounded to 2 decimal places.
    """
    variance = sum((num - mean) ** 2 for num in numbers)
    return round(variance / len(numbers), 2) if numbers else 0


def calculate_standard_deviation(variance):
    """
    Calculates the standard deviation based on the given variance.

    Args:
        variance (float): The variance of the numbers.

    Returns:
        float: The standard deviation, rounded to 2 decimal places.
    """
    guess = variance / 2
    for _ in range(20):  # Newton-Raphson method
        guess = (guess + variance / guess) / 2
    return round(guess, 2)


def process_file(file_path):
    """
    Processes the file, calculates statistics, and outputs the results.

    Args:
        file_path (str): The path to the file containing the numeric data.
    """
    start_time = time.time()
    numbers = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    for line_number, line in enumerate(lines, 1):
        item = line.strip()
        try:
            numbers.append(float(item))
        except ValueError:
            print(f"Invalid data at line {line_number}: '{item}'")

    if not numbers:
        print("No valid data found in the file.")
        return

    # Calculate statistics
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    standard_deviation = calculate_standard_deviation(variance)

    # Measure elapsed time
    elapsed_time = time.time() - start_time

    # Prepare results
    results = (
        f"Mean: {mean}\n"
        f"Median: {median}\n"
        f"Mode: {', '.join(map(str, mode)) if mode else 'No mode'}\n"
        f"Variance: {variance}\n"
        f"Standard Deviation: {standard_deviation}\n"
        f"Time elapsed: {elapsed_time:.4f} seconds"
    )

    # Output results
    print(results)
    with open('StatisticsResults.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(results + '\n')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py file_with_data.txt")
    else:
        input_file_path = sys.argv[1]
        process_file(input_file_path)
