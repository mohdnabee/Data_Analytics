import os 
import shutil


# Folder path you want  to organize 
FOLDER_PATH = os.getcwd()  # Current working directory

#   File Type Mapping 

FILE_TYPE = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'], 
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Scripts': [ '.js', '.html', '.css', '.php'],
    # 'Others': []  # For files that don't match any category
    }    


#   Creates Folders if They  Don't Exist
for folder in FILE_TYPE.keys(): # Creates folders for each file type category
    folder_path = os.path.join(FOLDER_PATH, folder)  
    if not os.path.exists(folder_path): # os.path.exists() checks if the folder already exists  
        os.makedirs(folder_path)

# organize Files 
for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

    #  Skip Folders 
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    # print(os.path.splitext(file))
    file_ext =  os.path.splitext(file)[1].lower()

    for folder, extensions in FILE_TYPE.items():
        if file_ext in extensions:
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))  # Move the file to the corresponding folder
         
print ("Files have been organized successfully!")  