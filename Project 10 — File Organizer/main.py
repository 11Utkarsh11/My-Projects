import os
import shutil

folder = r"U:\Programming\My Projects\Project 10 — File Organizer"

files = os.listdir(folder)

for file in files:
    extension = os.path.splitext(file)[1]
    full_path = os.path.join(folder, file)
    # print(f"{file} --> {os.path.isfile(full_path)} --> {extension}")

    if extension.lower() == ".txt" or extension.lower() == ".docx" or extension.lower() == ".doc":
        # print("Documents")
        doc = os.path.isdir(os.path.join(folder, "Documents"))
        if doc == False:
            docs = os.mkdir(os.path.join(folder, "Documents"))

        shutil.move(full_path, r"Project 10 — File Organizer\Documents")

    elif extension.lower() == ".jpg" or extension.lower() == ".jpeg" or extension.lower() == ".png":
        # print("Photos")
        photo = os.path.isdir(os.path.join(folder, "Photos"))
        if photo == False:
            photos = os.mkdir(os.path.join(folder, "Photos"))

        shutil.move(full_path, r"Project 10 — File Organizer\Photos")

    elif extension.lower() == ".mp3":
        # print("Audio")
        audio = os.path.isdir(os.path.join(folder, "Audios"))
        if audio == False:
            audios = os.mkdir(os.path.join(folder, "Audios"))

        shutil.move(full_path, r"Project 10 — File Organizer\Audios")

    elif extension.lower() == ".mp4":
        # print("Video")
        video = os.path.isdir(os.path.join(folder, "Videos"))
        if video == False:
            videos = os.mkdir(os.path.join(folder, "Videos"))

        shutil.move(full_path, r"Project 10 — File Organizer\Videos")

    else:
        continue
