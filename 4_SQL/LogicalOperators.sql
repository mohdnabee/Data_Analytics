USE ecom ; 
--  || ===========  Logical Operators in MySQL ================== ||  
-- USE IN --
-- select * from orders where city  IN('Delhi' ,'Mumbai') ; 
--  NOT IN --
-- SELECT * FROM orders  WHERE payment_mode  NOT IN('Cash' , 'UPI'); 
-- Using Between and Not Between --
-- SELECT * FROM orders WHERE price_per_unit BETWEEN 1000 AND 10000; 
-- SELECT * FROM orders WHERE price_per_unit NOT BETWEEN 1000 AND 10000;

-- || ============= Using like with Wildcard ========== || 

-- SELECT * FROM orders WHERE product LIKE "L%"  --  % wildcard  ( start with L) 
-- SELECT * FROM orders WHERE city LIKE "%hi" --  ends with hi 
-- SELECT * FROM orders WHERE city LIKE "%rab%" -- center rab  hon chaiya 
--  using _ wildcard ex =  d_lhi 
SELECT * FROM orders WHERE city LIKE "d_lhi" --  match  single character


