# 09 SQL - Employee Database

## Background

The goal was to create a SQL database from six CSV files that contain employees information.

### Data Modeling

An ERD diagram of the tables was created using http://www.quickdatabasediagrams.com.

![ERD](https://user-images.githubusercontent.com/77761497/175016182-86b790bb-469d-487a-88df-dd36b5857021.png)

### Data Engineering

A table SQL schema was created for each of the six CSV files.

### Data Analysis

Once I had a complete SQL database, the following information was extracted:

1. Employee's details: employee number, last name, first name, sex, and salary.
2. Employees who were hired in 1986: first name, last name, and hire date.
3. Manager of each department: department number, department name, the manager's employee number, last name, first name.
4. Department of each employee: employee number, last name, first name, and department name.
5. Employees whose first name is "Hercules" and last names begin with "B": first name, last name, and sex.
6. Employees in the sales department: employee number, last name, first name, and department name.
7. Employees in the sales and development departments: employee number, last name, first name, and department name.
8. In descending order, the frequency count of employees' last names.

The SQL database was then imported into pandas, and the following plots were created:

1. A histogram with the most common salary ranges for employees.
2. A bar chart of average salary by title.

## Skills

data engeneering | ERD diagram | SQL database | SQL queries | SQL table schemata
