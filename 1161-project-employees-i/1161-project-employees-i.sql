# Write your MySQL query statement below
select project_id, round(sum(experience_years)/count(experience_years),2) as average_years
from Employee
join Project using (employee_id)
group by project_id;

