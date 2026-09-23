use ecom ;  --  Stored Procedures in MySQL

-- Change the Delimiter
DELIMITER //

CREATE PROCEDURE get_delivered()
BEGIN
    SELECT *
    FROM orders
    WHERE order_status = 'Delivered';
    SELECT  * FROM employees;
END //

DELIMITER ; 