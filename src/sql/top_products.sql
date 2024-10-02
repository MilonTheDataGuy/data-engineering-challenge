SELECT 
    month, 
    product_id, 
    average_rating
FROM (
    SELECT 
        month, 
        product_id, 
        average_rating,
        DENSE_RANK() OVER (PARTITION BY month ORDER BY average_rating DESC) as RNK
    FROM RatingsMonthlyAggregates
)
WHERE RNK < 4;