# f = open("Chapter9/file.txt")
# print (f.read())
# f.close()

#  The Same can be written using with statement like This : 

with open("Chapter9/file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file 