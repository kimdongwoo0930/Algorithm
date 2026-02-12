# =====================================================================
#   18110번:    solved.ac
#   @date:   2026-02-06
#   @link:   https://www.acmicpc.net/problem/18110
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

"""
절사 평균이란 30%일 경우 위에서 15% 밑에서 15%를 제외하고 평균을 내어
사람수는 위 아래 밑에서 반올림 해야한다.
계산한 평균도 반올림한다.

1. 전체 n개를 입력받은후 15%의 인원을 구한다.
그후 위에서 밑에서 뺀다.
그 후 그거의 평균을 구하고 반올림하면 끝이다.
파이썬에서 반올림은 0.5 + int을 씌우는거다 .
"""


import sys

input = sys.stdin.readline
from collections import deque

N = int(input())
List = sorted(int(input()) for _ in range(N))
List = deque(List)
dump = int(N * 0.15 + 0.5)

for i in range(dump):
    List.pop()
    List.popleft()
if len(List) != 0:
    print(int(sum(List) / len(List) + 0.5))
else:
    print(0)
