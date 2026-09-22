try:
     a =  int (input ("Hey , Enter a number: "))
     print(a)

except ValueError as v:
     print("heyy")
    #  print(v)

except Exception as e: 
    print("Enter a valid Number ", e)

print("Thank You!!")



#  8 28 