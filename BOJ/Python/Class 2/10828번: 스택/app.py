# =====================================================================
#   10828번:    스택
#   @date:   2026-02-05
#   @link:   https://www.acmicpc.net/problem/10828
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

"""
N을 먼저 입력받아 횟수만큼 돌릴것이다.
"""


import sys

input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    S = input()
    if "push" in S:
        A, B = S.split()
        stack.append(B)
    elif "top" in S:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    elif "size" in S:
        print(len(stack))
    elif "empty" in S:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif "pop" in S:
        if len(stack) == 0:
            print(-1)
        else:
            A = stack.pop()
            print(A)
