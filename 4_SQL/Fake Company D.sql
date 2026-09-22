-- Create Database
CREATE DATABASE fake_company;

-- Use Database
USE fake_company;

-- Create Employees Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(100),
    department VARCHAR(50),
    job_role VARCHAR(50),
    salary INT,
    city VARCHAR(50),
    joining_date DATE
);

-- Insert Fake Data
INSERT INTO employees
(employee_name, department, job_role, salary, city, joining_date)
VALUES
('Rahul Sharma', 'IT', 'Android Developer', 45000, 'Indore', '2024-06-15'),
('Aman Khan', 'IT', 'Backend Developer', 52000, 'Bhopal', '2023-08-20'),
('Priya Singh', 'HR', 'HR Manager', 60000, 'Indore', '2022-03-10'),
('Arjun Verma', 'Sales', 'Sales Executive', 35000, 'Delhi', '2025-01-12'),
('Neha Gupta', 'Finance', 'Accountant', 48000, 'Mumbai', '2023-11-05'),
('Rohit Yadav', 'IT', 'Data Analyst', 55000, 'Pune', '2024-02-18'),
('Sneha Patel', 'Marketing', 'Marketing Executive', 40000, 'Ahmedabad', '2025-04-22'),
('Vikas Jain', 'IT', 'Software Engineer', 65000, 'Bangalore', '2022-09-14'),
('Anjali Mehta', 'Finance', 'Financial Analyst', 58000, 'Mumbai', '2024-07-01'),
('Karan Joshi', 'Sales', 'Sales Manager', 62000, 'Delhi', '2021-12-11');