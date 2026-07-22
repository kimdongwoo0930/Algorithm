# ☕ Java 문법 노트

> 문제를 푸는 게 목적이 아니라,
> **문제를 핑계로 Java 문법을 손에 익히는 게** 목적입니다.

코딩테스트 입문(Lv0)을 풀면서 새로 쓴 메서드, 헷갈렸던 문법을 여기에 누적합니다.
문제별 README에도 적고, 다시 볼 만한 것만 이 파일로 올립니다.

> ℹ️ 프로그래머스는 `class Solution`의 메서드만 채우는 방식이라
> BOJ처럼 `Scanner` / `BufferedReader`로 입력을 받을 일이 없습니다. 입출력 대신 **자료형과 API**에 집중합니다.

---

## 🔢 형변환

```java
int n = Integer.parseInt("123");    // String → int
String s = String.valueOf(123);     // int → String
String s2 = 123 + "";               // 같은 결과, 더 짧지만 덜 명시적
double d = (double) 3 / 2;          // 1.5  (캐스팅 안 하면 1)
```

### ✔ 배운 점

- `int / int`는 **소수점을 버린다**. `3 / 2 == 1`
- 음수 나눗셈은 0 방향으로 버림. `-3 / 2 == -1`, `-3 % 2 == -1`
- 값이 21억(`2^31-1`)을 넘을 것 같으면 `long`. 곱셈은 특히 주의

---

## 🔤 String

```java
s.length()              // 길이 (배열의 .length와 달리 괄호 있음)
s.charAt(i)             // i번째 문자 (char)
s.substring(a, b)       // a 이상 b 미만
s.contains("ab")
s.indexOf("a")          // 없으면 -1
s.replace("a", "b")
s.toUpperCase()
s.split(" ")            // String[] 로 자르기
s.split("")             // 한 글자씩 자르기
s.toCharArray()         // char[] 로
String.join(",", list)  // 합치기
```

### ✔ 배운 점

- 문자열 비교는 **반드시 `.equals()`** — `==`는 값이 아니라 주소를 비교한다
  → [로그인 성공?](./코딩테스트%20입문/문자열/로그인%20성공%3F)
- `split()`의 인자는 **정규식**이다. `.`이나 `|`로 자를 땐 `split("\\.")`처럼 escape
- 문자열은 불변(immutable)이라 반복문에서 `+=`로 이어붙이면 매번 새 객체가 생긴다 → `StringBuilder`

```java
StringBuilder sb = new StringBuilder();
for (int i = 0; i < n; i++) sb.append(i);
String result = sb.toString();

new StringBuilder(s).reverse().toString();  // 문자열 뒤집기
```

---

## 🔡 char 다루기

```java
char c = s.charAt(0);
int digit = c - '0';        // '7' → 7
int order = c - 'a';        // 'c' → 2  (알파벳 순서)
char next = (char) (c + 1); // 다음 글자 (캐스팅 필수)

Character.isDigit(c);
Character.isAlphabetic(c);
Character.toUpperCase(c);
```

### ✔ 배운 점

- `char`는 사실상 정수라서 산술이 된다. 단, 연산 결과는 `int`가 되므로 다시 `char`로 캐스팅해야 한다
- `'7' - '0'`이 7인 이유는 아스키 코드가 연속이기 때문

---

## 🔀 조건문

```java
switch (dir) {                    // Java 14+ : 화살표 형태, break 불필요
    case "left"  -> x -= 1;
    case "right" -> x += 1;
}

answer = 조건 ? "login" : "wrong pw";   // 삼항연산자 — 값을 고르는 if
```

### ✔ 배운 점

- 화살표 `switch`는 **break를 안 써도 fall-through가 없다.** 고전 `case ... :` 형태는
  `break`를 빠뜨리면 아래 case로 그대로 흘러내리므로 화살표 쪽이 안전하다 (Java 14+)
- `switch`의 조건으로 `String`을 넣을 수 있다 (Java 7+). 내부적으로 `.equals()` 비교라
  `==`의 함정이 없다
- 삼항연산자는 **분기해서 값을 정할 때** 쓴다. 분기해서 여러 줄을 실행할 땐 `if`가 낫다

→ [캐릭터의 좌표](./코딩테스트%20입문/조건문/캐릭터의%20좌표), [로그인 성공?](./코딩테스트%20입문/문자열/로그인%20성공%3F)

---

## 🔁 향상된 for문 (for-each)

```java
for (String dir : keyinput) { ... }     // 배열의 원소를 하나씩
for (String[] row : db) { ... }         // 2차원 배열은 "행"이 하나씩 나온다
```

### ✔ 배운 점

- 인덱스가 필요 없으면 향상된 for문이 짧고 실수가 적다
- `String[][]`를 돌리면 원소 타입이 `String`이 아니라 **`String[]`(행)** 이다.
  `row[0]`, `row[1]`로 열에 접근한다
- 반대로 **인덱스를 써야 하거나 원소를 수정해야 하면** 일반 for문을 써야 한다

→ [로그인 성공?](./코딩테스트%20입문/문자열/로그인%20성공%3F)

---

## 📦 배열

```java
int[] arr = new int[5];              // 0으로 초기화
int[] arr2 = {1, 2, 3};
arr.length                           // 길이 (괄호 없음)

Arrays.sort(arr);                    // 오름차순 정렬
Arrays.toString(arr);                // 출력용 문자열 (그냥 println하면 주소가 찍힌다)
Arrays.fill(arr, -1);                // 전부 채우기
Arrays.copyOfRange(arr, 1, 3);       // 1 이상 3 미만 잘라내기
```

### ✔ 배운 점

- `Arrays.sort(int[])`에는 **Comparator를 넣을 수 없다.** 내림차순이 필요하면 박싱해야 한다

  ```java
  Integer[] boxed = {3, 1, 2};
  Arrays.sort(boxed, Collections.reverseOrder());
  ```

- 배열은 `.length`, 문자열은 `.length()`, 컬렉션은 `.size()` — 셋 다 다르다
- 2차원 배열: `int[][] m = new int[3][4];` → `m.length`는 행, `m[0].length`는 열

---

## 🧺 컬렉션

```java
List<Integer> list = new ArrayList<>();
list.add(1); list.get(0); list.size(); list.contains(1);

Map<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.getOrDefault("b", 0);            // 없으면 기본값
map.merge("a", 1, Integer::sum);     // 카운팅에 유용
map.containsKey("a");

Set<Integer> set = new HashSet<>();   // 중복 제거
```

### ✔ 배운 점

- 제네릭에는 원시 타입을 못 쓴다. `List<int>` ❌ → `List<Integer>` ⭕
- 빈도수 세기는 `merge`가 가장 짧다

  ```java
  for (String w : words) map.merge(w, 1, Integer::sum);
  ```

---

## 🌊 배열 ↔ 리스트 (스트림)

```java
// int[] → List<Integer>
Arrays.stream(arr).boxed().collect(Collectors.toList());

// List<Integer> → int[]
list.stream().mapToInt(Integer::intValue).toArray();

// 자주 쓰는 연산
Arrays.stream(arr).sum();
Arrays.stream(arr).max().getAsInt();
Arrays.stream(arr).filter(n -> n % 2 == 0).toArray();
```

### ✔ 배운 점

- `int[]`와 `Integer[]`는 다른 타입이다. 이 변환이 자바 코테에서 제일 자주 걸리는 지점
- 스트림은 짧지만 느리다. 성능이 빡빡한 문제는 for문이 안전

---

## ➗ Math

```java
Math.abs(-3);       // 3
Math.max(a, b);
Math.min(a, b);
Math.pow(2, 10);    // 1024.0 — double 반환! int로 쓰려면 캐스팅
Math.sqrt(16);      // 4.0
Math.floor / ceil / round
```

### ✔ 배운 점

- `Math.pow`는 `double`을 반환하므로 `(int) Math.pow(2, 10)`으로 캐스팅해야 한다
