# Write your MySQL query statement below
select 
IFNULL(
(select Salary 
from employee
group by salary
order by salary desc
LIMIT 1 OFFSET 1),
null) as  SecondHighestSalary ;


