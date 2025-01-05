SELECT 
  ROUND(SUM(preferred = 'immediate') * 100.0 / COUNT(*), 2) AS immediate_percentage
FROM (
  SELECT
    customer_id,
    CASE 
      WHEN DATEDIFF(MIN(order_date), MIN(customer_pref_delivery_date)) = 0 THEN 'immediate'
      ELSE 'scheduled'
    END AS preferred
  FROM
    Delivery
  GROUP BY
    customer_id
) AS T;