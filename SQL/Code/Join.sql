USE sql_practice;

# JOIN 은 여러 테이블의 데이터를 연결해서 조회하는 기능
SELECT m.name, o.member_id, o.price
FROM members m
INNER JOIN orders o ON m.id = o.member_id;

# 교집합이라고 생각하고 해면 되긴한다.
USE sql_practice;
SELECT m.name, o.member_id, o.price
FROM members m
INNER JOIN orders o ON o.member_id = m.id;

# inner 생략가능
USE sql_practice;
SELECT m.name, o.member_id, o.price
FROM members m
JOIN orders o ON o.member_id = m.id;

# 여러조건
USE sql_practice;

