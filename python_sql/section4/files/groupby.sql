SELECT
  sex,
  COUNT(*),
  SUM(age),
  AVG(age)
FROM
  user
GROUP BY
  sex