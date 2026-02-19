# 
-- 1)
-- members에서 모든 회원의 id, name, age 조회

-- 2)
-- members에서 이메일 컬럼만 조회하되, 컬럼명을 메일로 별칭 붙이기

-- 3)
-- orders에서 상품명(product_name)과 가격(price) 만 조회

USE sql_practice;
SELECT * FROM members

SELECT 
    email AS 이메일
FROM members

SELECT product_name, price FROM orders


-- 2단계: WHERE (조건 필터링)
-- 4)
-- 나이가 30 이상인 회원의 name, age 조회

-- 5)
-- 가입일이 2024-02-01 이후(포함) 인 회원의 name, join_date 조회

-- 6)
-- 이름에 "김" 이 들어가는 회원의 id, name 조회
-- (시작이 아니라 “포함”)

-- 7)
-- 주문 가격이 100,000 이상인 주문의 product_name, price 조회

-- 8)
-- 상품명이 '노트북'으로 시작하는 주문만 조회
-- (예: 노트북, 노트북 파우치, 노트북 백팩, 노트북 거치대, 노트북 쿨러 등)

SELECT name,age FROM members WHERE age >=30

SELECT name, join_date FROM members WHERE join_date >= '2024-02-01'

SELECT id, name FROM members WHERE name LIKE "%김%"

SELECT product_name, price FROM orders WHERE price >= 100000

SELECT * from orders WHERE product_name LIKE "노트북%"

--  3단계: ORDER BY (정렬)
-- 9)
-- 회원 나이 기준 내림차순 정렬해서 name, age 조회

-- 10)
-- 주문을 price 내림차순으로 정렬해서 product_name, price 조회

-- 11)
-- price 내림차순, 같은 가격이면 order_date 오름차순 정렬

-- 정렬은 ORDER BY

SELECT name, age FROM members ORDER BY age DESC 

SELECT product_name, price FROM orders ORDER BY price DESC

SELECT order_date, price FROM orders ORDER BY price DESC , order_date ASC

-- 4단계: LIMIT / OFFSET (상위/페이징)
-- 12)
-- 가장 비싼 주문 상위 5개의 product_name, price 조회

-- 13)
-- 가장 비싼 주문 기준으로 6번째~10번째 (5개) 가져오기
-- (= LIMIT + OFFSET)

-- 14)
-- 가장 최근 주문 10개 조회 (order_date 기준 내림차순)

SELECT product_name, price FROM orders ORDER BY price DESC LIMIT 5

SELECT product_name, price FROM orders ORDER BY price DESC LIMIT 5 OFFSET 5

SELECT product_name, price, order_date FROM orders ORDER BY order_date DESC LIMIT 10

-- 5단계: DISTINCT (중복 제거)
-- 15)

-- 주문한 적 있는 member_id를 중복 없이 조회

-- 16)

-- orders에서 product_name을 중복 없이 조회 (상품 종류 리스트 만들기)


SELECT DISTINCT * FROM members

SELECT DISTINCT member_id FROM orders

SELECT DISTINCT product_name FROM orders


-- 17)

-- orders에서

-- 가격이 50,000 이상 200,000 이하

-- order_date가 2024-03-01 ~ 2024-03-31 사이
-- 인 주문의 product_name, price, order_date 조회
-- (힌트: BETWEEN 2번)

-- 18)

-- orders에서
-- 상품명이 아래 중 하나인 주문만 조회:

-- '웹캠'

-- '마이크'

-- '조명'
-- (힌트: IN)

-- 19)

-- members에서

-- 나이 25~30 사이

-- 이름에 “우” 포함
-- 인 회원을 age 오름차순으로 조회


SELECT product_name, price , order_date FROM orders
WHERE price BETWEEN 50000 AND 200000 AND
order_date BETWEEN "2024-03-01" AND "2024-03-31"


SELECT product_name FROM orders WHERE product_name IN ('웹캠', '마이크', '조명')


SELECT * FROM members WHERE age BETWEEN 25 AND 30 AND name LIKE "%우%" ORDER BY age ASC