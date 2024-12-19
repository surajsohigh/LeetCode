# Write your MySQL query statement below
select Prices.product_id, COALESCE( round( (sum(price*units)/sum(units) ), 2) , 0) as average_price from prices
left join UnitsSold
on UnitsSold.product_id = Prices.product_id
and purchase_date between start_date and end_date
group by product_id;

