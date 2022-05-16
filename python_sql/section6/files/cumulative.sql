SELECT
    action_date,
    COUNT(uid) as user_count,
    SUM(COUNT(uid)) OVER(
        ORDER BY action_date 
        ROWS BETWEEN UNBOUNDED PRECEDING
            AND CURRENT ROW
    ) AS cumulative
FROM
    user_action_log
GROUP BY 
    action_date