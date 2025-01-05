# Write your MySQL query statement below

select left(trans_date, 7) as month, 
country, 
count(trans_date) as trans_count,
sum(state='approved') as approved_count,
sum(amount) as trans_total_amount,
sum((state = "approved")*amount) as approved_total_amount
from Transactions as T
group by month, country;



