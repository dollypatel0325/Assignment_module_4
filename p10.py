# Specify the path to your output file
file_path = 'output.txt'  # Replace with the desired output file path

# Sample list of strings
my_list = ["Apple", "Banana", "Orange", "Grapes", "Mango"]

def write_list_to_file(file_path, my_list):
    try:
        # Open the file in write mode ('w')
        with open(file_path, 'w') as file:
            # Write each element of the list to the file
            for item in my_list:
                file.write(item + '\n')  # Add a newline for each item

        print(f"List has been written to '{file_path}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Write the list to the file
write_list_to_file(file_path, my_list)
