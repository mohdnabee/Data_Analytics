import os 
# select  the directory  whose contents you want to list
directory = "/wall paper/spide"
#use the os module to list the directory contents
contents = os.listdir(directory)

# print the contenst  of the directory
for item in contents:
    print(item)
# print (contents)