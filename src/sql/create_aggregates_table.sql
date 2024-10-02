CREATE TABLE IF NOT EXISTS RatingsMonthlyAggregates (
    month TEXT,
    product_id INT,
    average_rating INT
) ;

INSERT INTO RatingsMonthlyAggregates (month, product_id, average_rating)
SELECT
    strftime('%m',timestamp) as month,
    product_id,
    round(AVG(rating),1) as average_rating
FROM Ratings
GROUP BY month, product_id;