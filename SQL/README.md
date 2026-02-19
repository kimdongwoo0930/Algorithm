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


