USE ecom ; 

-- ||  ======= Aggregate Functions =================  || 

-- SELECT COUNT(*)  FROM  orders ; --  COUNT FUNCTION 
-- SELECT SUM(quantity * price_per_unit) AS total_revenue FROM orders; --  sum function 
-- SELECT  AVG(price_per_unit) From orders;  --  average function
-- SELECT MIN(price_per_unit) 	AS min_price  , MAX(price_per_unit) AS max_price  FROM orders;  -- min and max functions 


-- ||  ========    Scalar Functions  ======================   ||
 
-- SELECT customer_name, ROUND(price_per_unit, 0) FROM orders;   --  Round Functions 
-- SELECT UPPER(customer_name) , LOWER(city) FROM orders ;   --  Upper and Lower Function 
-- SELECT customer_name , LENGTH(customer_name) FROM orders ;   --  Length Function 


-- || ============  DATE FUNCTIONS ============================ || 
-- `SELECT CURRENT_DATE;-- CURRENT DATE FUNCTION   	

-- SELECT order_id, DATEDIFF(delivery_date, order_date) AS delivery_days FROM orders; -- DATEDIFF function 



SELECT * FROM orders wHERE YEAR(order_date) = 2025;  -- Using Functions with WHERE
