# Specify the path to your text file
file_path = 'example.txt'  # Replace with the actual path to your file

try:
    # Prompt the user to enter the number of lines to read
    n = int(input("Enter the number of lines to read: "))

    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Read the first n lines of the file
        first_n_lines = [file.readline().strip() for _ in range(n)]

    # Print the first n lines
    print(f"\nFirst {n} Lines of the File:")
    for line in first_n_lines:
        print(line)

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")

except ValueError:
    print("Please enter a valid number.")

except Exception as e:
    print(f"An error occurred: {e}")
