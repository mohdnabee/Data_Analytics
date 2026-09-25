items =  ["apple" , "banana" , "cherry"]
prices = [0.5 , 0.3 , 0.2] 

dict_prices = {items[i] : prices[i]  for i  in range (len(items) )}

print(dict_prices)