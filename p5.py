# Specify the path to your text file
file_path = 'example.txt'  # Replace with the actual path to your file

def read_file_lines(file_path):
    try:
        # Open the file in read mode ('r')
        with open(file_path, 'r') as file:
            # Read lines from the file and store them in a list
            lines = file.readlines()

        return lines

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Read lines from the file and store them in a list
file_lines = read_file_lines(file_path)
if file_lines is not None:
    print("Lines from the File:")
    for line in file_lines:
        print(line.strip())
