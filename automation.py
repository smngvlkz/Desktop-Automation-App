import os
import shutil

# Set the path to the downloads folder
downloads_path = 'C:/Users/smngv/Downloads'

# Set the paths to the destination folders
movies_path = 'C:/Users/smngv/Videos/Movies'
music_path = 'C:/Users/smngv/Music'
documents_path = 'C:/Users/smngv/Documents'
pictures_path = 'C:/Users/smngv/OneDrive/Pictures/Downloaded'

# Create a dictionary to map file extensions to destination folders
folders = {
    '.mkv': movies_path,
    '.mp4': movies_path,
    '.mp3': music_path,
    '.exe': documents_path,
    '.pdf': documents_path,
    '.png': pictures_path,
    '.jpeg': pictures_path,
    '.jpg': pictures_path
}

# Iterate over the files in the downloads folder
for filename in os.listdir(downloads_path):
    # Get the file extension
    file_ext = os.path.splitext(filename)[1]
    
    # Check if the file extension is in the dictionary
    if file_ext in folders:
        # Get the source and destination paths
        src_path = os.path.join(downloads_path, filename)
        dst_path = os.path.join(folders[file_ext], filename)
        
        # Move the file to the destination folder
        shutil.move(src_path, dst_path)
