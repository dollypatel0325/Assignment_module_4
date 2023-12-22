# Specify the paths for the source and destination files
source_file_path = 'source.txt'  # Replace with the actual path of your source file
destination_file_path = 'destination.txt'  # Replace with the desired path for the destination file

def copy_file(source_path, destination_path):
    try:
        # Open the source file in read mode ('r')
        with open(source_path, 'r') as source_file:
            # Read the entire content of the source file
            content = source_file.read()

            # Open the destination file in write mode ('w')
            with open(destination_path, 'w') as destination_file:
                # Write the content to the destination file
                destination_file.write(content)

        print(f"File copied from '{source_path}' to '{destination_path}'.")

    except FileNotFoundError:
        print(f"One of the files was not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Copy the contents from the source file to the destination file
copy_file(source_file_path, destination_file_path)
