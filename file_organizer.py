import os
import shutil

folder_path = r"C:\Users\AYUSH SINGH\Downloads"

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "ZIP Files": [".zip", ".rar", ".7z"],
    "Python Files": [".py"],
    "Other": []
}


def get_category(file_extension):
    for category, extensions in file_categories.items():
        if file_extension.lower() in extensions:
            return category

    return "Other"


def organize_files():

    if not os.path.exists(folder_path):
        print("Folder does not exist!")
        return

    files = os.listdir(folder_path)

    for file_name in files:

        file_path = os.path.join(folder_path, file_name)

        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(file_name)

        category = get_category(extension)

        category_folder = os.path.join(folder_path, category)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        destination = os.path.join(category_folder, file_name)

        shutil.move(file_path, destination)

        print(f"Moved: {file_name} → {category}/")


if __name__ == "__main__":
    organize_files()

    print("\nFile organization completed successfully!")