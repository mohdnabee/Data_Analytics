use ecom; 
-- set SQL_SAFE_UPDATES =0 ; 
update orders 

SET discount_percent = 10,
    rating = 4
WHERE customer_name = 'Neha Verma' and order_status = 'Delivered';
select * from  orders; 
