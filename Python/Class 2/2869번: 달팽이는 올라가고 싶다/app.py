# =====================================================================
#   2869번:    달팽이는 올라가고 싶다
#   @date:   2026-01-31
#   @link:   https://www.acmicpc.net/problem/2869
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

import sys

input = sys.stdin.readline

A, B, V = map(int, input().split())

if A >= V:
    print(1)
else:
    up = A - B
    days = (V - A + up - 1) // up + 1
    print(days)
