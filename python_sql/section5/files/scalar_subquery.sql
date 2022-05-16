SELECT
  *
FROM
  purchase_log
WHERE
  quantity > (
    SELECT
      AVG(quantity)
    FROM
      purchase_log
  )