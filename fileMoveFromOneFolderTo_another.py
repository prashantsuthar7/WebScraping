import os
import shutil
import datetime

# Define the source and destination paths
src_path = "C:/Users/prash/PycharmProjects/WebScraping"
dst_path = "C:/Users/prash/Downloads/testmove"

# Get the latest file in the source folder
text_files = [f for f in os.listdir(src_path) if f.endswith(".txt")]
print(text_files)
if text_files:
    latest_file = max(text_files, key=lambda f: os.path.getmtime(os.path.join(src_path, f)))
    # Construct the full path to the latest file
    src_file = os.path.join(src_path, latest_file)
    filename, file_extension = os.path.splitext(latest_file)
    # check if file already exists in destination path
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
    dst_file = os.path.join(dst_path, filename + '_' + timestamp + file_extension)
    if os.path.exists(dst_file):
        dst_file = os.path.join(dst_path, filename + '' + timestamp + '' + file_extension)
    # Copy the file
    shutil.copy2(src_file, dst_file)
else:
    print("No text files found in the source folder.")
