# Specify the path to your text file
file_path = 'example.txt'  # Replace with the actual path to your file

def count_lines(file_path):
    try:
        # Open the file in read mode ('r')
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Count the number of lines
            line_count = len(lines)

        return line_count

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Count the number of lines in the file
num_lines = count_lines(file_path)
if num_lines is not None:
    print(f"The file has {num_lines} line(s).")
