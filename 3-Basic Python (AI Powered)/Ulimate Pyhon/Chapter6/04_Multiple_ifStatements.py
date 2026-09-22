a= int(input("Enter Your age "))
#  Is statemnt no: 1 
if(a % 2 == 0):
    print("a is even")

#  end of if statemnt no: 1 

#  Is statemnt no: 2
if (a >= 18): 
    print("You are above the age of consent")
    print("Good For You")

elif(a < 0):
     print("You are entering an invalid nagative age ")

elif(a == 0):
     print("You are entering 0  which is not a valid age")

else :
      print("You are below the age of consent")

#  end of if statemnt no: 2

print("end of the program")