use ecom  ;  
UPDATE orders
SET order_status = 'Cancelled'
WHERE order_id = 2;

SELECT * FROM order_cancellations;
SELECT * FROM orders; 


-- DROP TRIGGER trg_log_order_cancel;
-- drop  table order_cancellation; 