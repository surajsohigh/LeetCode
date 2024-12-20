# Write your MySQL query statement below


select name from 
(
select e1.name, sum(case
when e1.id=e2.managerId then 1 else 0
end) as countNo 
from employee e1, employee e2
group by e1.id
) as subquery
where countNo >=5;

