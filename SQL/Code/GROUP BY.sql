USE sql_practice

SELECT member_id, COUNT(*) AS 주문횟수
FROM orders GROUP BY member_id


SELECT member_id, product_name, COUNT(*) AS 주문횟수
FROM orders GROUP BY member_id , product_name


SELECT member_id, SUM(price) AS 총액
FROM orders GROUP BY member_id
ORDER BY 총액 DESC

SELECT member_id, COUNT(*) AS 주문횟수
FROM orders
GROUP BY member_id
HAVING COUNT(*) >= 2


SELECT member_id, AVG(price)AS 평균
FROM orders
WHERE price >= 1000
GROUP BY member_id
HAVING AVG(price) >= 5000