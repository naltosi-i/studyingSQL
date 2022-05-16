SELECT
    action_date,
    COUNT(uid) as user_count,
    AVG(COUNT(uid)) OVER(
        ORDER BY action_date 
        ROWS BETWEEN 1 PRECEDING
            AND CURRENT ROW
    ) AS moving_average
FROM
    user_action_log
GROUP BY 
    action_date
