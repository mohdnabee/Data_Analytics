use fake_company; 

-- 1. Show all employees
-- SELECT * FROM employees;

-- 2. Show only employee name and salary
-- SELECT employee_name, salary FROM employees;

-- 3. Find employees from IT
-- SELECT * FROM employees
-- WHERE department = 'IT';

-- -- 4. Find employees earning more than 50,000
-- SELECT * FROM employees
-- WHERE salary > 50000;

-- 5. Find employees from Mumbai
-- SELECT * FROM employees
-- WHERE city = 'Mumbai';

-- -- 6. Sort employees by highest salary
-- SELECT * FROM employees
-- ORDER BY salary DESC;

-- -- 7. Count employees in each department
-- SELECT department, COUNT(*) AS total_employees
-- FROM employees
-- GROUP BY department;

-- -- 8. Find the highest salary
-- SELECT MAX(salary) AS highest_salary
-- FROM employees;

-- -- 9. Find the average salary
-- SELECT AVG(salary) AS average_salary
-- FROM employees;