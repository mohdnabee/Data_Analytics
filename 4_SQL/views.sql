-- CREATE VIEW delivered_orders AS
-- SELECT order_id,
--        customer_name,
--        city,
--        product,
--        price_per_unit,
--        order_date
-- FROM orders
-- WHERE order_status = 'Delivered';

-- UPDATE delivered_orders 
-- SET price_per_unit =  price_per_unit + 101 
-- WHERE order_id =  1 ; 

-- select * FROM  delivered_orders;

DROP  VIEW delivered_orders; 
DROP  VIEW del_mum_clients; 