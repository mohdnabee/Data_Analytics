n =  int (input ("Enter The Number:- "))

for i in range (2 , n):
    if (n% i) == 0 :
        print("The Number is Not prime!!! ")
        break
else:
    print ("Number Is Prime ....")