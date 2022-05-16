SELECT
    purchase_date,
    quantity,
    SUM(quantity) OVER(PARTITION BY purchase_date),
    MAX(quantity) OVER(PARTITION BY purchase_date),
    MIN(quantity) OVER(PARTITION BY purchase_date),
    AVG(quantity) OVER(PARTITION BY purchase_date),
    COUNT(quantity) OVER(PARTITION BY purchase_date)
FROM
    purchase_log
