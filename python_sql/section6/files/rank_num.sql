SELECT
    *,
    RANK() OVER(ORDER BY quantity),
    DENSE_RANK() OVER(ORDER BY quantity),
    ROW_NUMBER() OVER(ORDER BY quantity)
FROM
    purchase_log