-- select * from orders order by price_per_unit ;  -- incerasing order  me gaya ga 0.
-- select * from orders order by price_per_unit  DESC;  -- Descreasing Order  me agaya  ga 
-- select * from orders order by delivery_date  desc;
-- select * from orders order by city  desc , price_per_unit 
-- select * from orders order by city  desc , price_per_unit limit 5 ;  --  top  5 
select * from orders order by city  desc , price_per_unit limit 5 offset 5;  --   skip top  5 
