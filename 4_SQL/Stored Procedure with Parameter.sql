-- Stored Procedure with Parameter
use ecom ;
DELIMITER //

CREATE PROCEDURE get_orders_by_city(IN city_name VARCHAR(50))
BEGIN
    SELECT *
    FROM orders
    WHERE city = city_name;
END //

DELIMITER ;