
CREATE DATABASE company_revenue;

USE company_revenue;

CREATE TABLE company (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    company_name VARCHAR(100) NOT NULL,
    industry VARCHAR(50),
    city VARCHAR(50),
    revenue DECIMAL(15,2),
    expenses DECIMAL(15,2),
    employees INT,
    year INT
);


INSERT INTO company
(company_name, industry, city, revenue, expenses, employees, year)
VALUES
('TechNova', 'Technology', 'Bhopal', 8500000, 5200000, 120, 2024),
('GreenLeaf', 'Agriculture', 'Jabalpur', 4200000, 2800000, 75, 2024),
('AutoMax', 'Automobile', 'Indore', 12000000, 8500000, 200, 2024),
('DataVision', 'Technology', 'Pune', 9500000, 6100000, 150, 2025),
('FreshMart', 'Retail', 'Jabalpur', 6500000, 4700000, 90, 2025),
('SkyBuild', 'Construction', 'Bhopal', 15000000, 11000000, 250, 2025),
('MediCare', 'Healthcare', 'Indore', 7800000, 4900000, 110, 2024),
('CloudSoft', 'Technology', 'Bangalore', 18000000, 10500000, 300, 2025),
('Foodies', 'Food', 'Pune', 5500000, 3600000, 80, 2024),
('PowerGrid', 'Energy', 'Bhopal', 22000000, 16000000, 400, 2025),
('AutoMax', 'Automobile', 'Indore', 14500000, 9800000, 220, 2025),
('TechNova', 'Technology', 'Bhopal', 11000000, 6500000, 140, 2025),
('GreenLeaf', 'Agriculture', 'Jabalpur', 5000000, 3100000, 85, 2025),
('MediCare', 'Healthcare', 'Indore', 9000000, 5500000, 125, 2025),
('FreshMart', 'Retail', 'Jabalpur', 7200000, 5100000, 100, 2026);


SELECT * FROM company;

