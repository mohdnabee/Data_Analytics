import os 
# specify  the directory you want to list the files of
directory = "/wall paper/spide"
# list the files in the specified directory
contents = os.listdir(directory)

# print each  file and  directory name 
for item in contents:
    print(item)