import os


def get_creation_time(file_path):
    return os.path.getmtime(file_path)


def rename_and_sort_files(folder_path):
    # check if the path is a folder
    if not os.path.isdir(folder_path):
        print(f"{folder_path} is not a valid folder.")
        return

    # get folder name
    folder_name = os.path.basename(folder_path)

    # list all files and filter by creation date
    files = sorted(os.listdir(folder_path), key=lambda x: get_creation_time(
        os.path.join(folder_path, x)))

    # Browse files of the folder
    for index, file in enumerate(files, start=1):
        # Build the new name of the file using the current folder followed by the index
        new_name = f"{folder_name}_{index}{os.path.splitext(file)[1]}"

        # get the last file path
        old_path = os.path.join(folder_path, file)

        # get the new file path
        new_path = os.path.join(folder_path, new_name)

        # Rename file
        os.rename(old_path, new_path)

        print(
            f"The file {file} in {folder_name} folder has been rename to {new_name}")


dossier_a_analyser = input("Path to the folder: ")

rename_and_sort_files(dossier_a_analyser)
