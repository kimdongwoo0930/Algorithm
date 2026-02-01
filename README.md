# 🚀 알고리즘 학습 로그 (Python)

> 단순히 문제를 푸는 것이 아니라
> 더 빠르고, 더 깔끔한 해결 방법을 기록합니다.

이 저장소는 알고리즘 문제 풀이 과정에서

새롭게 알게 된 Python 표준 모듈, 최적화 기법, 문제 해결 사고 방식을 정리한 공간입니다.

---

## 📚 학습한 Python 모듈 정리

### ⚙️ sys — 빠른 입출력 처리

대량의 입력이 주어지는 환경에서
**시간 초과를 방지하기 위해 필수적**으로 사용했습니다.

```python
import sys
input = sys.stdin.readline
```

- `input()`보다 `sys.stdin.readline()`이 더 빠르다.
- BOJ 환경에서 성능 차이가 크다.

반복적인 출력을 할경우 `print()`보다 `sys.stdout.write()`를 사용하는게 좋다.

```python
out = sys.stdout.write
out(str(result) + '\n')
```

---

### 🧮 math — 수학적 사고 단순화

반복문을 줄이고
**수식 기반으로 문제를 해결**하기 위해 사용했습니다.

```python
import math
```

자주 사용하는 함수

```python
math.gcd(a, b)     # 최대공약수
math.lcm(a, b)     # 최소공배수
math.sqrt(n)       # 제곱근
math.factorial(n)  # 팩토리얼
```

#### ✔ 배운 점

- gcd를 사용하면 유클리드 호제법을 직접 구현할 필요가 없다
- 소수 판별은 sqrt(n)까지만 확인하면 충분하다
- 수학 라이브러리를 활용하면 코드가 간결해지고 안정성이 높아진다

---

### 🧺 collections — 문제에 맞는 자료구조

기본 자료구조 대신
**문제 성격에 맞는 자료구조를 선택해 성능**을 개선했습니다.

```python
from collections import Counter, deque
```

사용하는 함수

```python
Counter(arr)   # 빈도수 계산
deque()        # BFS, 양방향 큐
```

#### ✔ 배운 점

- Counter는 카운팅 정렬 및 빈도 문제에서 매우 효율적
- deque는 리스트보다 삽입/삭제 성능이 안정적
