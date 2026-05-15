# =====================================================================
#   10773번:    제로
#   @date:   2026-02-05
#   @link:   https://www.acmicpc.net/problem/10773
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================
"""
stack 그냥 꺼내기만 하면되는거엿다 ㅎㅎ


"""


import sys

input = sys.stdin.readline

N = int(input())
stack = []
List = [int(input()) for _ in range(N)]

for i in List:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))
