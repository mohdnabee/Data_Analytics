# Write a program to find out whether a given post is talking about “Harry” or not.

post  = input("Enter the Post: ")

if("Harry".lower() in post):
    print("This post is talking about harry")
else:
    print("This post is not talking about harry")