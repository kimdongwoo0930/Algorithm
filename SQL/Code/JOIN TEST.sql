-- 문제 1 (쉬움)
-- "주문한 회원의 이름, 나이, 주문 상품명, 가격을 조회하세요."

USE sql_practice;

SELECT m.name, m.age, o.product_name, o.price
FROM members m
INNER JOIN orders o ON m.id = o.member_id

-- "각 회원의 총 주문 금액을 조회하세요. (이름, 총 주문 금액)"

SELECT m.name, SUM(o.price) AS 총액
FROM members m
INNER JOIN orders o ON m.id = o.member_id
GROUP BY m.id, m.name

-- "주문을 2개 이상 한 회원의 이름과 주문 개수를 조회하세요."

SELECT m.name , COUNT(o.member_id)
FROM members m
INNER JOIN orders o ON m.id = o.member_id
GROUP BY m.id , m.name
HAVING COUNT(o.member_id) >= 2


-- 한 번도 주문한 적 없는 회원의 이름과 이메일을 조회하세요
USE sql_practice;

SELECT m.name, m.email
FROM members m
LEFT JOIN orders o ON m.id = o.member_id  -- 어떤 컬럼?
WHERE o.member_id IS NULL;              -- 어떤 컬럼이 NULL이면 주문 없는 사람?


-- 총 구매금액이 100,000원 이상인 회원의 이름과 총 구매금액을 조회하세요. 금액 높은 순으로 정

USE sql_practice;
SELECT m.name,  SUM(o.price)
FROM members m
INNER JOIN orders o ON m.id = o.member_id
GROUP BY m.name, m.id
HAVING SUM(o.price) >= 100000
ORDER BY SUM(o.price) DESC