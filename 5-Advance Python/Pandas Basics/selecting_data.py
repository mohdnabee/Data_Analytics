import pandas as pd  
data =  { 
    "name" :  ["Ali" ,"Sara" , "John" , "Deepali" , "Rakshita" , "Jack" , "James"],
    "marks" : [85, 90, 78,33,45,56,78]
}

df =  pd.DataFrame (data)
# print(df["marks"])
print(df[["name","marks"]])