import  pandas as pd 

df =  pd.DataFrame({
    'OrderID': [1, 2, 3, 4, 5],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Camera'],
    'Quantity': [1, 2, 1, 3, 1],
    'Price': [1000, 500, 300, 150, 700],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})


df.to_csv('ecommerce_orders.csv',mode ="a", header = True , index=False)