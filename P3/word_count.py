"""
Module: word_count.py
Description: This script reads a file, counts the frequency of each distinct word,
             sorts them in descending order of frequency, and outputs the results
             to both the console and a file named 'WordCountResults.txt'.
"""

import sys
import time


def count_words(words):
    """Count the frequency of each distinct word in the list."""
    word_frequency = {}
    for word in words:
        word = word.lower()  # Normalize to lowercase
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency


def process_file(input_file_path):
    """Process the file to count word frequencies and measure execution time."""
    start_time = time.time()
    word_frequency = {}
    total_words = 0

    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    for word in line.strip().split():
                        total_words += 1
                        word = word.lower()
                        word_frequency[word] = word_frequency.get(word, 0) + 1
                except ValueError as e:
                    print(f"Error processing line: {str(e)}")

    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        return

    sorted_word_frequency = sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)
    elapsed_time = time.time() - start_time

    # Prepare results
    results = "Word Frequency:\n"
    results += "\n".join(f"{word}: {count}" for word, count in word_frequency.items())

    results += "\n\nOrdered from Highest to Lowest Frequency:\n"
    results += "\n".join(f"{word}: {count}" for word, count in sorted_word_frequency)

    results += f"\n\nTotal Words Counted: {total_words}\n"
    results += f"Time elapsed: {elapsed_time:.4f} seconds"

    # Output to console
    print(results)

    # Output to file
    with open('WordCountResults.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(results + '\n')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python word_count.py fileWithData.txt")
    else:
        process_file(sys.argv[1])
