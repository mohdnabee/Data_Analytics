use ecom ;  
-- Sorts groups based on aggregated values.

SELECT city, order_status, COUNT(*) AS count
FROM orders
GROUP BY city, order_status
order by city  ,  order_status;