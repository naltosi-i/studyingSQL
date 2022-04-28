SELECT
  first_action_date,
  COUNT(uid)
FROM
  (
    SELECT
      uid,
      MIN(action_date) AS first_action_date
    FROM
      user_action_log
    GROUP BY
      uid
  )
GROUP BY
  first_action_date
ORDER BY
  first_action_date