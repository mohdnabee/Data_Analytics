-- SELECT customer_name, city, quantity FROM orders where discount_percent < 20 ; 
-- SELECT * FROM orders where discount_percent > 20 ; 
-- SELECT *FROM orders where delivery_date  is  NULL ; 
-- SELECT *FROM orders where city ='Delhi' AND order_status ='Delivered' ; 
-- SELECT *FROM orders where city ='Delhi' or order_status ='Delivered' ; 

SELECT customer_name, order_date, price_per_unit FROM orders ORDER BY order_date DESC;
