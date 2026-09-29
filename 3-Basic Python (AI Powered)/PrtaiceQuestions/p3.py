# Write a python program to display a user entered name followed by Good 
# Afternoon using input () function. 

name  =  input("Enter  The Name : ")
print(f"Good Afternoon {name}")

# Write a program to fill in a letter template given below with name and date. 
letter = f'''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
'''
print (letter.replace("<|Name|>", name).replace("<|Date|>", "29/09/2026"))

# Write a program to detect double space in a string.
text  = "this is a  space  text "
print(text.find(" "))