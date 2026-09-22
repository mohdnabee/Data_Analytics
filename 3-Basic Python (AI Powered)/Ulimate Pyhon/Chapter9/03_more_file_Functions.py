f = open("Chapter9/file.txt")

# lines = f.readlines()# readlines() reads the file line by line and returns a list of lines
# print(lines, type(lines))

# line1 =  f.readline()
# print(line1, type(line1))

# line2 =  f.readline()
# print(line2, type(line2))

# line3 =  f.readline()
# print(line3, type(line3))

#   Using Loop  
line = f.readline()
while(line != ""):
    print(line)
    line= f.readline()
f.close()

# 6:10:12