use ecom ; 
-- delete from   sellers 
-- where seller_id = 2 ; 

-- alter  table orders 
-- drop  foreign key fk_orders_seller; 

alter table orders 
Add constraint fk_orders_seller
foreign key (seller_id)
references sellers(seller_id) 
-- on delete set  null  ;  
on delete cascade ; 



select * from  orders;