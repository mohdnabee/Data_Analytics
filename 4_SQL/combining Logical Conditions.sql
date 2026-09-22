-- || ==== Combining logical condition =========== || 
SELECT *
FROM orders
WHERE category IN ('Electronics', 'Furniture')
AND price_per_unit NOT BETWEEN 5000 AND 20000; 