import os

# Define the directory containing the files
directory = '/my-directory'

# Initialize a counter
counter = 1

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Get the file extension
    file_extension = os.path.splitext(filename)[1]

    # Construct the new file name
    # You can choose however you want to rename the file, jo rogan is an example
    new_filename = f'joe-rogan-real-{counter}{file_extension}'

    # Construct the full old and new file paths
    old_file_path = os.path.join(directory, filename)
    new_file_path = os.path.join(directory, new_filename)

    # Rename the file
    os.rename(old_file_path, new_file_path)

    # Increment the counter
    counter += 1

print("File renaming complete.")