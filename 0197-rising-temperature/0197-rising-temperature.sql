# Write your MySQL query statement below

select t1.id from Weather t1, Weather t2
where DATEDIFF(t1.recordDate, t2.recordDate) = 1
and t1.temperature > t2.temperature;

