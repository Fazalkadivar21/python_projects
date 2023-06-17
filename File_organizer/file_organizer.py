import os
import shutil


def file_org():
    cwd = input("Enter the path to organize: ")

    # you can add more extensions in this dict manually or do as asked in the readme file at last
    file_search = {
        ".txt": "Text Documents",
        ".doc": "Word Documents",
        ".xls": "Excel files",
        ".ppt": "PowerPoint Presentation",
        ".pdf": "Portable Document Format",
        ".jpg": "Images",
        ".png": "Images",
        ".m4a": "Audio Files",
        ".gif": "Graphics Interchange Format Image",
        ".bmp": "Images",
        ".mp3": "Audio Files",
        ".wav": "Audio Files",
        ".mp4": "Videos",
        ".zip": "Archive Files",
        ".exe": "Executable Files",
        ".html": "HTML Files",
        ".css": "CSS Files",
        ".js": "JavaScript Files",
        ".xml": "XML Files",
        ".json": "JavaScript Object"
    }

    valid_extensions = set(file_search.keys())

    for entry in os.scandir(cwd):
        if entry.is_file():
            file_name, file_extension = os.path.splitext(entry.name)
            file_extension = file_extension.lower()

            if file_extension in valid_extensions:
                destination_folder = os.path.join(cwd, file_search[file_extension])
                os.makedirs(destination_folder, exist_ok=True)
                destination_path = os.path.join(destination_folder, entry.name)
                shutil.move(entry.path, destination_path)


file_org()
