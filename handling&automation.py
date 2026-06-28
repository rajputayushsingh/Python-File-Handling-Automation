import os
import shutil
import csv

# -------------------------------
# Create sample text file
# -------------------------------
try:
    with open("sample.txt", "w") as file:
        file.write("Hello, Welcome to Python File Handling!\n")
        file.write("This file is created automatically.")

    print("sample.txt created successfully.")

except Exception as e:
    print("Error creating text file:", e)

# -------------------------------
# Read text file
# -------------------------------
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print("\nText File Content:")
        print(content)

except FileNotFoundError:
    print("sample.txt not found.")

# -------------------------------
# Create CSV file
# -------------------------------
try:
    with open("students.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Name", "Marks"])
        writer.writerow([1, "Ayush", 90])
        writer.writerow([2, "Rahul", 85])
        writer.writerow([3, "Priya", 95])

    print("\nstudents.csv created successfully.")

except Exception as e:
    print("CSV Error:", e)

# -------------------------------
# Rename File
# -------------------------------
try:
    os.rename("sample.txt", "renamed_sample.txt")
    print("File renamed successfully.")

except FileNotFoundError:
    print("File not found for renaming.")

# -------------------------------
# Create Backup Folder
# -------------------------------
try:
    if not os.path.exists("Backup"):
        os.mkdir("Backup")

    shutil.move("renamed_sample.txt", "Backup/renamed_sample.txt")
    print("File moved to Backup folder.")

except Exception as e:
    print("Move Error:", e)

# -------------------------------
# Delete CSV File
# -------------------------------
try:
    os.remove("students.csv")
    print("students.csv deleted successfully.")

except FileNotFoundError:
    print("CSV file not found.")

print("\nAutomation Completed Successfully!")