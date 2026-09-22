use fake_company  ; 

-- CREATE TABLE product (
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     product_name VARCHAR(50),
--     price_per_unit INT,
--     qty INT,
--     sales INT GENERATED ALWAYS AS (price_per_unit * qty) STORED
-- );

INSERT INTO product (product_name, price_per_unit, qty)
VALUES
('Laptop', 50000, 7),
('Mouse', 500, 10),
('Keyboard', 1000, 12),
('Laptop Skin'  , 300 , 20), 
('pendrive' , 350 ,  10 ), 
('RGB keybord' , 1500 , 3), 
('RGB MOUSE'  , 1000 , 3) , 
('Mouse Pad ' , 50  , 10 );  

select *  from   product; 