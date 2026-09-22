items =  ["apple","apple",  "banana" , "orange" ,]
# print(items)
# items [1] = "grapes"
# print(items)

#  Methods 
# print (len(items))

#   1st  
# items.append("Kiwi") #  append method is used to add a new value at the end of the list
# print (items)

#  2nd 
# items.insert(1,"mango")
#  3rd 
# items.extend(["watermelon" , "papaya"]) #  extend method is used to add multiple values at the end of the list

#   4th  
# items.remove("banana") #  remove method is used to remove a value from the list
# print (items)

#   5th  pop 
# items.pop(2) #  pop method is used to remove a value from the list based on index
# print (items)

# 6th  clear
# items.clear()
# print(items)


# print(items.index("mango")) #  index method is used to find the index of a value in the list

# print (items.count("apple")) #  count method is used to find the number of occurrences of a value in the list



#  sort  list 
numbers = [5, 2, 9, 1, 5, 6] 
print(numbers)
numbers.sort() #  sort method is used to sort the list in ascending order
print(numbers)
numbers.sort(reverse=True) #  sort method is used to sort the list in descending order
print(numbers)

#  in is a membership operator in python
print (9 in numbers ) #  in operator is used to check if a value is present in the list or not  