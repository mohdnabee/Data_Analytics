#   pip  install  pandas

import pandas as pd  
data =  { 
    "name" :  ["Ali" ,"Sara" , "John" , "Deepali" , "Rakshita" , "Jack" , "James"],
    "marks" : [85, 90, 78,33,45,56,78]
}

#  data frame 

df =  pd.DataFrame(data) #  tabluar  data form  
# print(df.head())
# print(df.tail())
print(df.describe())

# print (df)