use ecom ; 

-- UPDATE  orders SET  seller_id = null  WHERE order_id IN (1,9,11) ; 

select 
o.order_id , o.product , o.city As customer_city  , 
s.seller_name 
from  orders o
right  JOIN sellers s
ON o.seller_id =  s.seller_id;


-- SELECT  * FROM orders ; -- 