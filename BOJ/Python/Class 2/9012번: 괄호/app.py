# =====================================================================
#   9012번:    괄호
#   @date:   2026-02-05
#   @link:   https://www.acmicpc.net/problem/9012
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    Input = list(input().strip())
    stack = []
    Bool = True
    for i in Input:
        if i == "(":
            stack.append("(")
        else:
            if len(stack) != 0:
                A = stack.pop()
                if A == "(":
                    continue
                else:
                    Bool = False
                    break
            else:
                Bool = False
                break

    if len(stack) != 0:
        Bool = False

    if Bool:
        print("YES")
    else:
        print("NO")
