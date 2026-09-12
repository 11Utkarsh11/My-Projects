import os
import shutil


# The folder we want to organize
folder = r"U:\Programming\My Projects\Project 10 — File Organizer"


def extension_checker(extension):
    """
    Decide which category the file belongs to
    based on its extension.
    """

    extension = extension.lower()

    if extension == ".txt" or extension == ".docx" or extension == ".doc":
        return "Documents"

    elif extension == ".jpg" or extension == ".jpeg" or extension == ".png":
        return "Photos"

    elif extension == ".mp3":
        return "Audios"

    elif extension == ".mp4":
        return "Videos"

    else:
        return None


def file_moving(file_path, category):
    """
    Create the category folder if necessary,
    then move the file into it.
    """

    # Build the destination folder path
    destination = os.path.join(folder, category)

    # Create the folder only if it doesn't already exist
    if not os.path.isdir(destination):
        os.mkdir(destination)

    # Move the file into the destination folder
    shutil.move(file_path, destination)


def main():
    # Get everything inside our target folder
    files = os.listdir(folder)

    # Process every item one at a time
    for file in files:

        # Build the complete path of the current item
        full_path = os.path.join(folder, file)

        # Ignore folders and only work with actual files
        if not os.path.isfile(full_path):
            continue

        # Extract the extension
        extension = os.path.splitext(file)[1]

        # Figure out which category this extension belongs to
        category = extension_checker(extension)

        # Ignore extensions that our organizer doesn't support
        if category is None:
            continue

        # Move the file to its category folder
        file_moving(full_path, category)


# Start the program
main()