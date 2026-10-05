import  pandas as pd 

# pip  install  openpyxl

df =  pd.read_csv('data.csv')
# print(df)

#  selected all  deliverd orders 
# delivered_orders = df[df['order_status'] == 'Delivered']
# print(delivered_orders)


#  selected all  deliverd orders  from Bangolore
delivered_orders = df[(df['order_status'] == 'Delivered') & (df['city'] == 'Bangalore')]
print(delivered_orders)