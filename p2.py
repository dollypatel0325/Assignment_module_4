# Specify the path to your text file
file_path = 'example.txt'  # Replace with the actual path to your file

try:
    # Open the file in append mode ('a')
    with open(file_path, 'a') as file:
        # Get text to append from the user
        text_to_append = input("Enter text to append to the file: ")

        # Append the text to the file
        file.write(text_to_append + '\n')  # Add a newline for clarity

    # Open the file again in read mode ('r') to display the updated content
    with open(file_path, 'r') as file:
        # Read the entire content of the file
        file_content = file.read()

        # Print the updated content
        print("\nUpdated File Content:")
        print(file_content)

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
