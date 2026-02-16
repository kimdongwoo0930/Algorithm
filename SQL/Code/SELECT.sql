SELECT * FROM members

SELECT age, name FROM members 

SELECT 
    name AS 이름,
    age AS 나이,
    email AS 이메일
FROM members;

WHERE age >= 30;

# 매번 안해주면 전에 기준으로 계산이 된다.
SELECT name, age 
FROM members 
WHERE age >= 25 AND age <=30;
# AND 또는 BETWEEN 사용하기
SELECT name, age 
FROM members 
WHERE age BETWEEN 25 AND 30;


# 25세 또는 30세인경우
SELECT name, age 
FROM members 
WHERE age = 25 OR age = 30;

SELECT name, age 
FROM members 
WHERE age In(25,30)

SELECT name, age FROM members
WHERE name LIKE "김%"

SELECT name, age FROM members
WHERE name LIKE "김__"

SELECT name FROM members
WHERE email IS NULL

SELECT name FROM members
WHERE email IS NOT NULL
