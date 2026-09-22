USE ecom  ;  --  subqueries means query  written  iniside another  query 
--   This query  is shows the average value is greater  
-- SELECT  * FROM  orders 
-- WHERE price_per_unit > (
-- SELECT  AVG(price_per_unit) FROM orders);

--  show the electronocs sales order city  
-- SELECT  * FROM orders 
-- WHERE city IN(
-- SELECT  city  FROM orders where category  =  "Electronics") ; 

-- shows column  avg 
 
--  SELECT  order_id , customer_name ,  price_per_unit , 
--  (SELECT  AVG(price_per_unit) FROM orders) AS avearge 
--  FROM orders ; 

--  SELECT  * , 
--  (SELECT  AVG(price_per_unit) FROM orders) AS avearge 
--  FROM orders ; 

-- furniture orders city   uisng exists 
SELECT *
FROM orders o
WHERE EXISTS (
    SELECT 1
    FROM orders
    WHERE city = o.city
      AND category = 'Furniture'
);


