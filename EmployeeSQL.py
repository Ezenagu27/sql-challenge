-- Create new table for public_departments
CREATE TABLE public_departments(
	id SERIAL PRIMARY KEY,
	dept_no VARCHAR NOT NULL,
	dept_name VARCHAR NOT NULL
	FOREIGN KEY (dept_no)REFERENCES department_employees(dept_no)
	FOREIGN KEY (dept_no)REFERENCES department_managers(dept_no)
);
SELECT*
FROM public_departments;

-- Create new table for Employees
CREATE TABLE department_employees(
	id SERIAL PRIMARY KEY,
	emp_no INT NOT NULL,
	dept_no VARCHAR NOT NULL,
	FOREIGN KEY emp_no
	FOREIGN KEY dept_no
);
SELECT*
FROM department_employees

-- Create new table for Managers
CREATE TABLE department_managers(
	id SERIAL PRIMARY KEY,
	dep_no VARCHAR NOT NULL,
	emp_no INT NOT NULL
	FOREIGN KEY dept_no

);
SELECT *
FROM department_managers

-- Create new table for Employees
CREATE TABLE public_employees(
	id SERIAL PRIMARY KEY,
	emp_no INT NOT NULL,
	emp_title_id VARCHAR NOT NULL ,
	birth_date VARCHAR NOT NULL,
	first_name VARCHAR NOT NULL,
	last_name VARCHAR NOT NULL,
	sex VARCHAR NOT NULL,
	hire_date DATE NOT NULL
);
SELECT *
FROM public_employees

-- Create new table for Salaries
CREATE TABLE salaries(
	id SERIAL PRIMARY KEY,
	emp_no VARCHAR NOT NULL,
	salary VARCHAR NOT NULL
);
SELECT *
FROM salaries
-- Create new table for Title
CREATE TABLE title(
	id SERIAL PRIMARY KEY,
	title_id VARCHAR NOT NULL,
	title VARCHAR NOT NULL
);
SELECT *
FROM title
--List the employee number, last name, first name, sex, and salary of each employee.

ALTER TABLE public_employees
DROP COLUMN hire_date;

SELECT *
FROM public_employees

SELECT public_employees.emp_no, salaries.salary
FROM public_employees
INNER JOIN salaries ON public_employees.emp_no = salaries.emp_no;


--List the first name, last name, and hire date for the employees who were hired in 1986.
SELECT first_name, last_name, hire_date
FROM public_employees
WHERE hire_date > '01/01/1985'
AND hire_date < '01/01/1986';

--List the manager of each department along with their department number, department name, employee number, last name, and first name.
SELECT d.dep_no, d.dept_name, e.emp_title_id, e.last_name, e.first_name
FROM department_employees.d
JOIN public_employees.e ON d.dep_no = e.emp_title_id;

--List the department number for each employee along with that employee’s employee number, last name, first name, and department name.
SELECT e.employee_id, e.last_name, e.first_name, d.department_id, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

--List first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B.
SELECT first_name, last_name, sex
FROM public_employees
WHERE first_name = 'Hercules' AND last_name LIKE 'B%';

--List each employee in the Sales department, including their employee number, last name, and first name.
SELECT emp_no, last_name, first_name
FROM public_departments
WHERE dept_name = 'Sales';