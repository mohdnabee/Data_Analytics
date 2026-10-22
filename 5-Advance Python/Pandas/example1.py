import  pandas  as pd  

mydataset  =  { 
    'cars' : ["BMW",'VOLVO' ,'FORD'], 
    'passings' : [3,7,2] 
}

myvar  =   pd.DataFrame(mydataset)
print (myvar)