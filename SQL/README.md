# 🗄️ SQL 학습 로그

> 단순한 쿼리 암기가 아니라,
> 왜 이렇게 작성하는지 이해하고 기록합니다.

이 폴더는 MySQL 환경에서 직접 실습하며
SELECT부터 집계 함수까지 SQL 핵심 개념을 정리한 공간입니다.

---

## 🛠️ 실습 환경

- **DB**: MySQL
- **환경**: VSCode + Docker (MySQL 컨테이너)

---

## 📚 학습 내용 정리

### 1️⃣ SELECT — 기초 데이터 조회

SQL의 가장 기본이자 핵심 명령어.

```sql
-- 전체 조회
SELECT * FROM members;

-- 특정 컬럼만 조회
SELECT name, age FROM members;

-- 별칭 붙이기
SELECT name AS 이름, age AS 나이 FROM members;
```

---

### 2️⃣ WHERE — 조건 필터링

```sql
-- 기본 조건
SELECT name, age FROM members WHERE age >= 30;

-- AND / OR
SELECT name, age FROM members WHERE age >= 25 AND age <= 30;

-- BETWEEN
SELECT name, age FROM members WHERE age BETWEEN 25 AND 30;

-- IN
SELECT name, age FROM members WHERE age IN (25, 30);

-- LIKE (문자열 검색)
SELECT name FROM members WHERE name LIKE '김%';   -- '김'으로 시작
SELECT name FROM members WHERE name LIKE '%우%';  -- '우' 포함

-- NULL 처리
SELECT name FROM members WHERE email IS NULL;
SELECT name FROM members WHERE email IS NOT NULL;
```

#### ✔ 배운 점

- `= NULL`은 항상 false → 반드시 `IS NULL` 사용
- 문자열은 반드시 작은따옴표(`'`)로 감싸야 한다
- `%`는 여러 문자, `_`는 정확히 1개 문자를 의미

---

### 3️⃣ ORDER BY — 정렬

```sql
-- 오름차순 (기본값)
SELECT name, age FROM members ORDER BY age ASC;

-- 내림차순
SELECT name, age FROM members ORDER BY age DESC;

-- 다중 정렬 (나이 내림차순, 같으면 이름 오름차순)
SELECT name, age FROM members ORDER BY age DESC, name ASC;
```

---

### 4️⃣ LIMIT / OFFSET — 개수 제한 및 페이징

```sql
-- 상위 5개만
SELECT product_name, price FROM orders ORDER BY price DESC LIMIT 5;

-- 6번째부터 5개 (페이징)
SELECT product_name, price FROM orders ORDER BY price DESC LIMIT 5 OFFSET 5;
```

---

### 5️⃣ DISTINCT — 중복 제거

```sql
-- 중복 제거
SELECT DISTINCT member_id FROM orders;

-- 여러 컬럼 조합으로 중복 제거
SELECT DISTINCT member_id, order_date FROM orders;
```

---

## 💡 SQL 실행 순서

SQL이 실제로 실행되는 순서는 작성 순서와 다르다.

```
1. FROM     - 어느 테이블에서?
2. WHERE    - 어떤 조건으로?
3. SELECT   - 어떤 컬럼을?
4. ORDER BY - 어떤 순서로?
5. LIMIT    - 몇 개만?
```

---

## ❌ 자주 하는 실수

```sql
-- WHERE와 ORDER BY 순서 틀림
SELECT * FROM members ORDER BY age WHERE age >= 30;  -- ❌ 에러

-- NULL 비교 잘못
WHERE email = NULL   -- ❌ 항상 false
WHERE email IS NULL  -- ✅

-- 문자열 따옴표 누락
WHERE name = 김동우   -- ❌ 에러
WHERE name = '김동우' -- ✅
```

---

### 6️⃣ GROUP BY & 집계 함수 — 그룹화 및 통계

데이터를 그룹으로 묶어서 통계를 내는 핵심 기능.

```sql
-- 집계 함수 기본
SELECT COUNT(*) FROM orders;              -- 전체 개수
SELECT COUNT(DISTINCT member_id) FROM orders;  -- 중복 제거 개수
SELECT SUM(price) FROM orders;            -- 합계
SELECT AVG(price) FROM orders;            -- 평균
SELECT MAX(price) FROM orders;            -- 최댓값
SELECT MIN(price) FROM orders;            -- 최솟값

-- GROUP BY로 그룹별 통계
SELECT member_id, COUNT(*) AS 주문횟수
FROM orders
GROUP BY member_id;

-- 여러 컬럼으로 그룹화
SELECT member_id, product_name, COUNT(*) AS 주문횟수
FROM orders
GROUP BY member_id, product_name;

-- 집계 함수와 정렬 조합
SELECT member_id, SUM(price) AS 총구매액
FROM orders
GROUP BY member_id
ORDER BY 총구매액 DESC;
```

#### ✔ 배운 점

- GROUP BY에 명시한 컬럼만 SELECT 가능 (+ 집계 함수)
- COUNT(*)는 NULL 포함, COUNT(컬럼)은 NULL 제외
- GROUP BY는 WHERE 이후, ORDER BY 이전에 실행됨

---

### 7️⃣ HAVING — 그룹 조건 필터링

WHERE는 개별 행 필터링, HAVING은 그룹 필터링.

```sql
-- 주문 2회 이상인 회원만
SELECT member_id, COUNT(*) AS 주문횟수
FROM orders
GROUP BY member_id
HAVING COUNT(*) >= 2;

-- WHERE + HAVING 조합
SELECT member_id, AVG(price) AS 평균구매액
FROM orders
WHERE price >= 1000        -- 개별 주문이 1000원 이상인 것만
GROUP BY member_id
HAVING AVG(price) >= 5000; -- 평균이 5000원 이상인 회원만
```

#### ✔ 배운 점

- WHERE: 그룹화 전 필터링 (개별 행)
- HAVING: 그룹화 후 필터링 (그룹 단위)
- 실행 순서: WHERE → GROUP BY → HAVING → ORDER BY

---

### 8️⃣ JOIN — 테이블 결합

여러 테이블의 데이터를 연결해서 조회하는 핵심 기능.

#### INNER JOIN — 교집합 (양쪽 모두 있는 데이터만)

```sql
-- 기본 INNER JOIN
SELECT m.name, o.product_name, o.price
FROM members m
INNER JOIN orders o ON m.id = o.member_id;

-- INNER는 생략 가능
SELECT m.name, o.product_name
FROM members m
JOIN orders o ON m.id = o.member_id;

-- 여러 조건 결합
SELECT m.name, o.product_name
FROM members m
JOIN orders o ON m.id = o.member_id
WHERE o.price >= 10000;
```

#### LEFT JOIN — 왼쪽 테이블 기준 (왼쪽은 전부, 오른쪽은 매칭되는 것만)

```sql
-- 주문 안 한 회원도 포함
SELECT m.name, o.product_name
FROM members m
LEFT JOIN orders o ON m.id = o.member_id;

-- NULL 체크로 "주문 안 한 회원" 찾기
SELECT m.name
FROM members m
LEFT JOIN orders o ON m.id = o.member_id
WHERE o.order_id IS NULL;
```

#### RIGHT JOIN — 오른쪽 테이블 기준

```sql
-- LEFT JOIN을 뒤집은 것과 같음 (잘 안 씀)
SELECT m.name, o.product_name
FROM members m
RIGHT JOIN orders o ON m.id = o.member_id;
```

#### 여러 테이블 JOIN

```sql
-- 3개 테이블 결합 (예시)
SELECT m.name, o.product_name, c.category_name
FROM members m
JOIN orders o ON m.id = o.member_id
JOIN categories c ON o.category_id = c.category_id;
```

#### ✔ 배운 점

- **INNER JOIN**: 양쪽 테이블에 모두 있는 데이터만 (교집합)
- **LEFT JOIN**: 왼쪽 테이블은 전부 + 오른쪽은 매칭되는 것만
- **RIGHT JOIN**: LEFT JOIN을 반대로 (실무에선 LEFT로 바꿔 씀)
- JOIN 조건은 `ON` 키워드로 명시
- 테이블 별칭(alias) 사용: `members m`, `orders o`
- LEFT JOIN + `WHERE xxx IS NULL` = "매칭 안 되는 데이터 찾기"

---


