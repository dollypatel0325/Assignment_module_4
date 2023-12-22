# Specify the path to your text file
file_path = 'example.txt'  # Replace with the actual path to your file

def read_last_n_lines(file_path, n):
    try:
        # Open the file in read mode ('r')
        with open(file_path, 'r') as file:
            # Read all lines from the file
            all_lines = file.readlines()

            # Calculate the starting index to read the last n lines
            start_index = max(0, len(all_lines) - n)

            # Get the last n lines
            last_n_lines = all_lines[start_index:]

        return last_n_lines

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Prompt the user to enter the number of lines to read
n = int(input("Enter the number of lines to read from the end: "))

# Read and print the last n lines
last_n_lines = read_last_n_lines(file_path, n)
if last_n_lines is not None:
    print(f"\nLast {n} Lines of the File:")
    for line in last_n_lines:
        print(line.strip())
