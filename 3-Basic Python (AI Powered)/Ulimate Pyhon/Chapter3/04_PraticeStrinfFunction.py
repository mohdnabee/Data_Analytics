#  1 convert case 
text =  "hello world"
print (text.upper()) # HELLO WORLD
print (text.lower()) # hello world
print (text.title()) # Hello World

# 2 Remove Spaces 
text1= "  Hello  "
print(text1.strip()) # "Hello"
print(text1.lstrip()) # "Hello  "
print(text1.rstrip()) # "  Hello"

# 3 Replace Text
text2= "I Like Java"
print (text2.replace("Java","Python")) # I Like Python

# 4 Find Text 
print(text.find("world")) # 6

# 5 Count Characters
text3 ="Nabeel"
print(text3.count("e")) # 2

#  6 Split Text
text4 = "apple,banana , oragane"
print (text4.split(",")) # ['apple', 'banana ', ' oragane']

# 7 Join Strings
words =  ["Hello", "World"]
print(" ".join(words)) # Hello World
