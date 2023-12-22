# Specify the path to your text file
file_path = 'example.txt'  # Replace with the actual path to your file

def find_longest_words(file_path):
    try:
        # Open the file in read mode ('r')
        with open(file_path, 'r') as file:
            # Read the entire content of the file
            content = file.read()

            # Split the content into words
            words = content.split()

            # Find the length of the longest word(s)
            max_word_length = len(max(words, key=len))

            # Filter words with the maximum length
            longest_words = [word for word in words if len(word) == max_word_length]

        return longest_words

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Find and print the longest words in the file
longest_words = find_longest_words(file_path)
if longest_words is not None:
    print("Longest Word(s):")
    for word in longest_words:
        print(word)
