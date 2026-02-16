USE sql_practice;

-- 전체 회원 조회
SELECT * FROM members;

-- 주문 내역 조회
SELECT * FROM orders;

-- 회원별 주문 금액 합계
SELECT 
    m.name,
    COUNT(o.order_id) AS order_count,
    SUM(o.price) AS total_price
FROM members m
LEFT JOIN orders o ON m.id = o.member_id
GROUP BY m.id, m.name
ORDER BY total_price DESC;

