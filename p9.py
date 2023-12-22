from collections import Counter
import string

# Specify the path to your text file
file_path = 'example.txt'  # Replace with the actual path to your file

def count_word_frequency(file_path):
    try:
        # Open the file in read mode ('r')
        with open(file_path, 'r') as file:
            # Read the entire content of the file
            content = file.read().lower()  # Convert to lowercase for case-insensitivity

            # Remove punctuation
            content = content.translate(str.maketrans('', '', string.punctuation))

            # Split the content into words
            words = content.split()

            # Count the frequency of each word
            word_frequency = Counter(words)

        return word_frequency

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Count the frequency of words in the file
word_frequency = count_word_frequency(file_path)
if word_frequency is not None:
    print("Word Frequency:")
    for word, count in word_frequency.items():
        print(f"{word}: {count}")
