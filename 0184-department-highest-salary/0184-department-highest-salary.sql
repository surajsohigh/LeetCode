# Write your MySQL query statement below

with cteTable as (select d.name as Department, e.name as Employee, Salary from Employee e
join Department d
on e.departmentId=d.id
)

-- select * from cteTable;

select Department, Employee, Salary from
(
select Department, Employee, Salary,
rank() over(partition by Department order by Salary desc) as rnk
from cteTable) t
where rnk=1;

