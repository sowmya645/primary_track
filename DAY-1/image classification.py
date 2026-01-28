import os
import shutil

# Destination backup folder
ne = r"C:\Users\91906\OneDrive\Desktop\primary track capg\backup_2"

# Create backup folder if not exists
if not os.path.exists(ne):
    os.mkdir(ne)

# Create subfolders for jpeg and png
jpeg_folder = os.path.join(ne, "b_jpeg")
png_folder = os.path.join(ne, "b_png")

os.makedirs(jpeg_folder, exist_ok=True)
os.makedirs(png_folder, exist_ok=True)

# Source folder containing images
source = r"C:\Users\91906\Downloads"

# Loop through files in source folder
for file in os.listdir(source):
    file_path = os.path.join(source, file)

    # Skip if it's not a file
    if not os.path.isfile(file_path):
        continue

    # Check extension and move accordingly
    if file.lower().endswith((".jpg", ".jpeg")):
        shutil.move(file_path, os.path.join(jpeg_folder, file))
    elif file.lower().endswith(".png"):
        shutil.move(file_path, os.path.join(png_folder, file))

print("Segregation complete ✅")