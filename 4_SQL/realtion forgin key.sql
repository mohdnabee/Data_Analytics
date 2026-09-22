use ecom  ; 
-- create Table sellers (
-- seller_id INT PRIMARY KEY auto_increment, 
-- seller_name varchar(100) unique not null, 
-- city varchar (50) );

INSERT INTO orders (seller_id, product, quantity, price_per_unit)
VALUES (2, 'Lamp', 14, 8000);

select * from orders; 