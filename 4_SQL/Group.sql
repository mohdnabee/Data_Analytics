use ecom ;  

-- SELECT city, COUNT(*) AS total_orders
-- FROM orders
-- GROUP BY city;

-- SELECT category, COUNT(*) AS total_orders
-- FROM orders
-- GROUP BY category;

-- SELECT category, COUNT(*) AS total_orders,  sum(quantity * price_per_unit ) as 	 total_sales
-- FROM orders
-- GROUP BY category;

-- SELECT city, COUNT(*) AS total_orders,  sum(quantity * price_per_unit ) as 	 total_sales
-- FROM orders
-- GROUP BY city;

-- SELECT city, AVG(price_per_unit)  as avg_price
-- FROM orders
-- GROUP BY city;


-- SELECT city, order_status, COUNT(*) AS count
-- FROM orders
-- GROUP BY city, order_status;