# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 


d = {} #  empty dictionary 

name = input ("Enter Friends name: ")
lang  = input ("Enter language name: ")
d.update({name:lang})

name = input ("Enter Friends name: ")
lang  = input ("Enter language name: ")
d.update({name:lang})

name = input ("Enter Friends name: ")
lang  = input ("Enter language name: ")
d.update({name:lang})

name = input ("Enter Friends name: ")
lang  = input ("Enter language name: ")
d.update({name:lang})

print (d)