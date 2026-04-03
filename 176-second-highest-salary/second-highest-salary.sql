# Write your MySQL query statement below
Select
(select Distinct Salary 
from employee
order by salary desc
LIMIT 1 OFFSET 1) as SecondHighestSalary;


