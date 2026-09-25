SELECT  COUNT(*)  AS cancelled 
FROM orders 
WHERE  order_status = 'Cancelled' 