
def greatest(a,b,c):
    if(a>b and c>a):
       return a
    elif(b>a and b>c):
       return b
    elif(c>b and c>a):
       return c
    
a =1 
b =21
c =3


print (greatest(a,b,c))