def complex_calc(i): 
    # some complex calculations here 
    return i*i



def  get_numbers() : 
    for i in range (5) : 
        yield complex_calc(i)

# for i in  get_numbers() : 
#     print(i)

a  =  get_numbers()
# print(a, type(a))
print(next(a)) 
print(next(a))
print(next(a))