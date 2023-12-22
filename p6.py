# Specify the path to your text file
file_path = 'example.txt'  # Replace with the actual path to your file

def read_file_lines(file_path):
    try:
        # Open the file in read mode ('r')
        with open(file_path, 'r') as file:
            # Read lines from the file and store them in a variable
            file_content = file.read()

        return file_content

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Read lines from the file and store them in a variable
file_content = read_file_lines(file_path)
if file_content is not None:
    print("File Content:")
    print(file_content)
