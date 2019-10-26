-- create table for departments
DROP TABLE IF EXISTS departments

CREATE TABLE departments (
dept_no VARCHAR PRIMARY KEY NOT NULL,
dept_name VARCHAR NOT NULL
)

-- create table for employees
DROP TABLE IF EXISTS employees

CREATE TABLE employees (
emp_no INT PRIMARY KEY NOT NULL,
birth_date VARCHAR NOT NULL,
first_name VARCHAR NOT NULL,
last_name VARCHAR NOT NULL,
gender VARCHAR NOT NULL,
hire_date VARCHAR NOT NULL
)

-- create table for deptartment managers
DROP TABLE IF EXISTS dept_manager

CREATE TABLE dept_manager (
dept_no VARCHAR NOT NULL,
emp_no INT NOT NULL,
FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
from_date VARCHAR NOT NULL,
to_date VARCHAR NOT NULL,
FOREIGN KEY (dept_no) REFERENCES departments(dept_no)
)

-- create table for salaries
DROP TABLE IF EXISTS salaries

CREATE TABLE salaries (
emp_no INT NOT NULL,
salary INT NOT NULL,
from_date VARCHAR NOT NULL,
to_date VARCHAR NOT NULL,
FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
)

-- create table for titles
DROP TABLE IF EXISTS titles

CREATE TABLE titles (
emp_no INT NOT NULL,
title VARCHAR NOT NULL,
from_date VARCHAR NOT NULL,
to_date VARCHAR NOT NULL,
FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
)

-- create table for deptartment employees
DROP TABLE IF EXISTS dept_emp

CREATE TABLE dept_emp (
emp_no INT NOT NULL,
dept_no VARCHAR NOT NULL,
from_date VARCHAR NOT NULL,
to_date VARCHAR NOT NULL,
FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
)

--display contents of each table
SELECT * FROM departments
SELECT * FROM dept_emp
SELECT * FROM dept_manager
SELECT * FROM employees
SELECT * FROM salaries
SELECT * FROM titles

--display employee number, last name, first name, gender, and salary by joining salaries and employees tables using the empployee number from both tables
SELECT employees.emp_no, employees.last_name, employees.first_name, employees.gender, salaries.salary
FROM salaries
JOIN employees ON
employees.emp_no = salaries.emp_no

--display hired employees from employees table using there WHERE function and % after the year to ignore months and days.
SELECT * FROM employees
WHERE hire_date LIKE '1986%'

--display the selected columns by inner joining the deptment numbers from dept_manager and departments table, and then employee numbers from the employees and dept_manager tables.
SELECT departments.dept_no, departments.dept_name, dept_manager.emp_no, employees.last_name, employees.first_name, dept_manager.from_date, dept_manager.to_date
FROM departments
JOIN dept_manager ON
dept_manager.dept_no = departments.dept_no
JOIN employees ON
employees.emp_no = dept_manager.emp_no

--use inner join on employee numbers in the employee no in the employees and deptment employees table and then join using the dept number
--from departments and dept_employees to find employeee and department details
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM employees
JOIN dept_emp ON
employees.emp_no = dept_emp.emp_no
JOIN departments ON
departments.dept_no = dept_emp.dept_no

--use where function in the empoyees table to find where Hercules in first_name  column is true and last_name column starts with B using % to ignore everything after B
SELECT * FROM employees
WHERE first_name LIKE 'Hercules'
AND last_name LIKE 'B%'

--display the selected columns using an inner join to connect the employyees and deptment employees tables using the empoyee number column, and then
--using the dept number to connect departments and deptment employees, and using the where function to narrow search to sales department
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM employees
JOIN dept_emp ON
employees.emp_no = dept_emp.emp_no
JOIN departments ON
departments.dept_no = dept_emp.dept_no
WHERE departments.dept_name LIKE 'Sales'

--display selected columns using inner joins where it is in the development department or sales department
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM employees
JOIN dept_emp ON
employees.emp_no = dept_emp.emp_no
JOIN departments ON
departments.dept_no = dept_emp.dept_no
WHERE departments.dept_name LIKE 'Development'
OR departments.dept_name LIKE 'Sales'

--display last_name column in employees table; count entire table using count(*) and rename to duplicate names; group by last name; order dup names in decending order
SELECT last_name, 
COUNT(*) AS duplicate_names
FROM employees
GROUP BY last_name
ORDER BY duplicate_names DESC