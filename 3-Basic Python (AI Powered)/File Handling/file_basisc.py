a =  "Nabeel  is Good"
date = "24-07-26"


# file =  open("Nabeel.txt","w")
# file.write(a)
# file.write(date)


file =  open("Nabeel.txt","r")
# content =  file.read()
content  =  file.readlines()
print(content)


file.close()