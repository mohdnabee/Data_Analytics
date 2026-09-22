#   List  are used to  store  multiple values in a single variable 

names =  ["GTA5" , "MK11" , "RISE OF EROS ", "WHERE WINDS MEET"]

elemnts = [1, 2,34,67 , False ,  True ]

# print (names) # print all the values in the list
# print (type(names))

# print (elemnts) # print all the values in the list

# print (elemnts[0])
# print (elemnts[1])

print (elemnts [1: 4]) # Slicing the list from index 1 to 3 (4 is not included)

print (len(elemnts)) 
#   List  in python are mutable 

elemnts [3]  =  69 
print (elemnts)