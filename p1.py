# Specify the path to your text file
file_path = 'example.txt'  # Replace with the actual path to your file

try:
    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Read the entire content of the file
        file_content = file.read()

        # Print the content
        print("File Content:")
        print(file_content)

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
