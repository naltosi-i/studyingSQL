SELECT
  uid,
  MIN(action_date) AS first_action_date
FROM
  user_action_log
GROUP BY
  uid