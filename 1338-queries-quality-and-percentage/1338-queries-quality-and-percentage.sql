
SELECT 
    query_name, 
    round(sum(rating/position)/count(query_name),2) as quality, 
    round (sum(case
    when rating < 3 then 1 else 0
    end)*100 / count(*), 2) as poor_query_percentage
FROM Queries
GROUP BY query_name; 


