name = "nabeel" 
print (len(name))

print (name.endswith("eel"))
print (name.startswith("NA"))
print(name.capitalize())



newName =  "mohd nabeel"
print(newName.title()) # first letter of each word will be capitalized

#   String.find(word) 
print(newName.find("nabeel")) # it will return the index of the first letter of the word


#   String.replace(old, new)
print(newName.replace("mohd", "mohammed")) # it will replace the old word with the new word in the string