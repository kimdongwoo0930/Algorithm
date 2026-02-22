
-- ## 📝 연습 문제

-- ### 문제 1: 인기 상품 TOP 3 (난이도: ⭐)

-- **orders 테이블**
-- | order_id | member_id | product_name | price |
-- |----------|-----------|--------------|-------|
-- | 1 | 1 | 노트북 | 50000 |
-- | 2 | 1 | 마우스 | 2000 |
-- | 3 | 2 | 노트북 | 50000 |
-- | 4 | 3 | 키보드 | 5000 |
-- | 5 | 2 | 마우스 | 2000 |
-- | 6 | 4 | 노트북 | 50000 |

-- **요구사항**: 판매량이 많은 상위 3개 상품과 판매 횟수를 조회하시오.

-- **결과**:
-- | product_name | 판매횟수 |
-- |--------------|----------|
-- | 노트북 | 3 |
-- | 마우스 | 2 |
-- | 키보드 | 1 |


USE sql_practice;

SELECT product_name, COUNT(*) AS 판매횟수
FROM orders
GROUP BY product_name
ORDER BY 판매횟수 DESC
LIMIT 3;

-- ---

-- ### 문제 2: VIP 회원 찾기 (난이도: ⭐⭐)

-- **요구사항**: 총 구매금액이 50000원 이상인 회원의 ID와 총 구매금액을 조회하시오. (금액 내림차순)

-- **결과**:
-- | member_id | 총구매액 |
-- |-----------|----------|
-- | 1 | 52000 |
-- | 2 | 52000 |


USE sql_practice;
SELECT member_id, SUM(price) AS 총구매액
FROM orders
GROUP BY member_id
HAVING SUM(price) >= 50000
ORDER BY SUM(price) DESC;



-- ---

-- ### 문제 3: 조건부 통계 (난이도: ⭐⭐⭐)

-- **요구사항**:
-- - 10000원 이상인 주문만 집계
-- - 평균 구매액이 30000원 이상인 회원만 조회
-- - 회원 ID, 주문 횟수, 평균 구매액 출력
-- - 평균 구매액 내림차순 정렬


-- **결과**:
-- | member_id | 주문횟수 | 평균구매액 |
-- |-----------|----------|------------|
-- | 3 | 1 | 50000.0000 |
-- | 1 | 1 | 50000.0000 |
-- | 2 | 1 | 50000.0000 |



USE sql_practice;
SELECT member_id, COUNT(*) AS 주문횟수, AVG(price) AS 평균구매액
FROM orders
WHERE price >= 10000
GROUP BY member_id
HAVING AVG(price) >= 30000
ORDER BY AVG(price) DESC