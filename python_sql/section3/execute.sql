SELECT
  *
FROM
  purchase_log
  LEFT JOIN user
  ON purchase_log.user_id=user.id
