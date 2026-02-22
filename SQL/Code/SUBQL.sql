-- 주문을 한 번이라도 한 회원의 이름과 나이를 조회하세요.

USE sql_practice;
SELECT m.name , m.age FROM members m
WHERE m.id  IN (SELECT member_id FROM orders)

-- 가장 비싼 주문의 회원 이름을 조회하세요.

SELECT m.name
FROM members m
WHERE m.id IN (
    SELECT member_id FROM orders o
    WHERE o.price = (
        SELECT MAX(price) FROM orders
    )
)


-- 전체 주문의 평균 금액보다 많이 쓴 주문의 상품명과 금액을 조회하세요.

SELECT o.product_name, o.price
FROM orders o
WHERE o.price >= (SELECT AVG(PRICE) FROM orders)

-- 회원별 총 구매금액을 구하고, 그 중 평균 총 구매금액보다 높은 회원의 이름과 총 구매금액을 조회하세요.

USE sql_practice;
SELECT m.name, sub.total
FROM members m
INNER JOIN (
    SELECT member_id, SUM(price) as total FROM orders 
    GROUP BY member_id
) AS sub ON m.id = sub.member_id
WHERE sub.total >= (SELECT AVG(price) FROM orders)


-- 주문을 2번 이상 한 회원의 이름, 주문 횟수, 총 구매금액을 조회하세요. 주문 횟수 높은 순으로 정렬.
USE sql_practice;
SELECT m.name, COUNT(o.order_id) AS 주문횟수, SUM(o.price) AS 총금액
FROM members m
INNER JOIN orders o ON m.id = o.member_id
GROUP BY m.id, m.name
HAVING COUNT(o.order_id) >= 2
ORDER BY 주문횟수 DESC
