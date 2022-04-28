WITH firtst_action AS (
  SELECT
    UID,
    MIN(action_date) AS first_action_date
  FROM
    user_action_log
  GROUP BY
    UID
)
SELECT
  first_action_date,
  COUNT(UID)
FROM
  firtst_action
GROUP BY
  first_action_date
ORDER BY
  first_action_date