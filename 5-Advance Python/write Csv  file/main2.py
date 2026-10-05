import  pandas as pd  
#  Create a DataFrame from of ecommerce orders 
df =  pd.DataFrame({
    'OrderID': [1, 2, 3, 4, 5],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Camera'],
    'Quantity': [1, 2, 1, 3, 1],
    'Price': [1000, 500, 300, 150, 700],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
})
#  create a DataFrame from of products 
df2 =  pd.DataFrame({
    'ProductID': [101, 102, 103, 104, 105],
    'ProductName': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Camera'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'Price': [1000, 500, 300, 150, 700],
    'Stock': [10, 20, 15, 30, 5]
})


# print(df)

with pd.ExcelWriter('ecommerce.xlsx') as writer: 
    df.to_excel(writer, sheet_name='Orders', index=False)
    df2.to_excel(writer, sheet_name='Products', index=False)