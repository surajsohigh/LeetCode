# Write your MySQL query statement below
select contest_id, round(count(user_id)*100/(select count(user_id) from Users),2)  as percentage
from register 
group by contest_id
ORDER BY percentage desc, contest_id;



