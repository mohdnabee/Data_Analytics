#  Write a program which finds out whether a given name is present in a list or not. 

l =  ["Harry" ,"Rohan", "Nabeel", "Shubham"]

name = input ("ENTER YOUR NAME: ")

if (name in l):
    print ("Your name is in the List")
else :
    print("Your name is not in the List")