import sys
import time


# Module docstring
"""This script reads a file containing decimal numbers, converts them to binary 
and hexadecimal, and writes the results to a new file with proper formatting.
Invalid data lines are flagged with error messages. It also reports the time
taken for the conversion process.
"""


def decimal_to_binary(n):
    """
    Convert a decimal number to its binary representation.
    """
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary


def decimal_to_hexadecimal(n):
    """
    Convert a decimal number to its hexadecimal representation.
    """
    if n == 0:
        return '0'
    hex_chars = '0123456789ABCDEF'
    hexadecimal = ''
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
    return hexadecimal


def process_file(input_file_path):
    """
    Process a file to convert each decimal number into binary and hexadecimal.
    The results are printed to the console and written to an output file.
    """
    start_time = time.time()

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        return

    results = []

    for line_number, line in enumerate(lines, 1):
        item = line.strip()
        try:
            number = int(item)
            binary = decimal_to_binary(number)
            hexadecimal = decimal_to_hexadecimal(number)
            result = f"{number}, {binary}, {hexadecimal}"
        except ValueError:
            error_message = f"Invalid data at line {line_number}: '{item}'"
            print(error_message)
            result = error_message
        results.append(result)

    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_time_message = f"Time elapsed: {elapsed_time:.4f} seconds"

    # Output to console
    for res in results:
        print(res)
    print(elapsed_time_message)

    # Output to file with separated columns
    with open('ConvertionResults.txt', 'w', encoding='utf-8') as output_file:
        output_file.write("Decimal, Binary, Hexadecimal\n")  # Header
        for res in results:
            output_file.write(res + '\n')
        output_file.write(elapsed_time_message + '\n')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
    else:
        file_path = sys.argv[1]
        process_file(file_path)
