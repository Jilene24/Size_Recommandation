import os


def rename_files_sequentially(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Sort the files to ensure they are renamed in a specific order
    files.sort()

    # Step 1: Rename all files to temporary names
    for i, filename in enumerate(files):
        # Split the filename into name and extension
        name, ext = os.path.splitext(filename)

        # Construct the temporary filename
        temp_name = f'temp_{i}{ext}'

        # Get the full old and temporary file paths
        old_path = os.path.join(directory, filename)
        temp_path = os.path.join(directory, temp_name)

        # Rename the file to the temporary name
        os.rename(old_path, temp_path)
        print(f'Renamed: {filename} to {temp_name}')

    # Step 2: Rename the temporary files to the final sequential names
    temp_files = os.listdir(directory)
    temp_files.sort()

    for i, temp_filename in enumerate(temp_files, start=1):
        # Split the temporary filename into name and extension
        name, ext = os.path.splitext(temp_filename)

        # Construct the final sequential filename
        final_name = f'{i}{ext}'

        # Get the full temporary and final file paths
        temp_path = os.path.join(directory, temp_filename)
        final_path = os.path.join(directory, final_name)

        # Rename the temporary file to the final name
        os.rename(temp_path, final_path)
        print(f'Renamed: {temp_filename} to {final_name}')


# Example usage
directory = r'C:\Users\Jilen\PycharmProjects\Size Recommendation\src\Data2\Not_oversize\long'
rename_files_sequentially(directory)
