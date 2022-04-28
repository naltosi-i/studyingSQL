SELECT
    *,
    RANK() OVER(ORDER BY quantity DESC)
FROM
    purchase_log
