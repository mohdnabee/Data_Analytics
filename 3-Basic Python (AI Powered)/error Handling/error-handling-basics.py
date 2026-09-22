print ("Initilaizing")

a =  int(input("Enter a: "))
b =  int(input("Enter b: "))

try:
    print ("the value of a/b is: " , a/b)
except Exception as e : 
    # print(e)
    print("Some error occurred!- " ,  e)
print ("Thank  you .!.!.!.")  