use fake_company; 

SELECT employee_id, employee_name
FROM employees
WHERE employee_name IN (
    SELECT employee_name
    FROM employees
    GROUP BY employee_name
    HAVING COUNT(*) > 1
)
ORDER BY employee_name;