# =====================================================================
#   1193번:    분수찾기
#   @date:   2026-03-31
#   @link:   https://www.acmicpc.net/problem/1193
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

import sys

input = sys.stdin.readline

"""
a/b -> 만약 b/a하고 같으면 -> 만약 a - b 가 음수면 b + 1 양ㅅ면 a + 1
매번 a > b - >  a - 1 b + 1 ) a < b a + 1 b - 1

1. A/B하고 b/a가 같은지 비교하기 -> 
2. 만약 같다면 a b 크기 비교하고  어디에 + 1ㅏㄹ지 지정 
3. 만약 다르다면 a b 크기 비교후 + 1 - 1 결정
이렇게 계속하다 N과 같은 cnt가 되면 그때의 값 
"""


N = int(input())
A, B = 1, 1
a, b = 1, 1
cnt = 0

Dire = True

while True:
    cnt += 1
    if cnt == N:
        print("{}/{}".format(a, b))
        break
    if A == b and B == a:
        if a > b:
            a += 1
        else:
            b += 1
        A, B, Dire = a, b, not Dire
    else:
        if not Dire:
            a += 1
            b -= 1
        else:
            a -= 1
            b += 1
