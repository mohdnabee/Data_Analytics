x=  78   #  global  variable 

def show_value(): 
    global x 
    x = 89 
    print (x)

show_value()
show_value()
print(x)