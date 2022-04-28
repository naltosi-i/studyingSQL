-- SELECT
--   SUBSTR(user_id, 4, 5)
-- FROM
--   purchase_log
-- ;

-- SELECT
--   LENGTH(NAME)
-- FROM
--   product
-- ;

-- SELECT
--   sex,
--   COUNT(*),
--   SUM(age),
--   AVG(age),
--   ROUND(AVG(age))
-- FROM
--   user
-- GROUP BY
--   sex
-- ;

SELECT
  purchase_log.*,
  COALESCE(user.id, 'データ無し'),
  COALESCE(user.sex, 'データ無し'),
  COALESCE(user.age, 'データ無し')
FROM
  purchase_log
  LEFT JOIN user
  ON purchase_log.user_id = user.id
;