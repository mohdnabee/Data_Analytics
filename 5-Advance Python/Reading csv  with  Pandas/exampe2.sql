USE company_revenue;

-- SELECT SUM(revenue) AS total_Revenue  FROM company;
-- SELECT *  From company order by revenue DESC  limit  1  ; 

SELECT
    company_name,
    revenue,
    expenses,
    revenue - expenses AS profit
FROM company;