--  HAVING Clause
-- HAVING is used to filter groups after aggregation.

SELECT city, order_status, COUNT(*) AS count
FROM orders
GROUP BY city, order_status
having city  in ('Delhi' ,  'Mumbai')

-- SELECT city, COUNT(*) AS total_orders
-- FROM orders
-- GROUP BY city
-- HAVING COUNT(*) > 5;