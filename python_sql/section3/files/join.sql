SELECT
  *
FROM
  purchase_log
  JOIN product
  ON purchase_log.product_id=product.id

