SELECT
  *
FROM
  purchase_log
  JOIN user
  ON purchase_log.user_id=user.id
