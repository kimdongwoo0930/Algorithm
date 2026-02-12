# =====================================================================
#   1929번:    소수 구하기
#   @date:   2026-02-06
#   @link:   https://www.acmicpc.net/problem/1929
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

"""
M 이상 N 이하 소수 구하기
"""

import sys

input = sys.stdin.readline


def sosu(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


N, M = map(int, input().split())
for i in range(N, M + 1):
    if i < 2:
        continue
    result = sosu(i)
    if result:
        print(i)
