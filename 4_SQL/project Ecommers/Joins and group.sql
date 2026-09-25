use harryshop ; 
-- select  SUM(amount )  as total_revenue  from  payments ; 

select  p.product_name ,  sum(oi.quantity * p.price) as revenue 
from  order_items oi  
join products p on  oi.product_id =  p.product_id
join orders o on oi.product_id = o.order_id 
where o.order_status = 'Delivered' 
group by p.product_name 
order by revenue desc	; 