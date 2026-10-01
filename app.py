from flask import Flask, render_template, request
import os
import shutil

app = Flask(__name__)

folder_path = "test_files"

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "ZIP Files": [".zip", ".rar", ".7z"],
    "Python Files": [".py"]
}


def get_category(extension):
    for category, extensions in file_categories.items():
        if extension.lower() in extensions:
            return category

    return "Other"


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        files = os.listdir(folder_path)

        for file_name in files:

            file_path = os.path.join(folder_path, file_name)

            if os.path.isdir(file_path):
                continue

            _, extension = os.path.splitext(file_name)

            category = get_category(extension)

            category_folder = os.path.join(folder_path, category)

            os.makedirs(category_folder, exist_ok=True)

            destination = os.path.join(category_folder, file_name)

            shutil.move(file_path, destination)

        message = "Files organized successfully!"

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)