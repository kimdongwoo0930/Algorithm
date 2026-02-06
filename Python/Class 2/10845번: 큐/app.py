# =====================================================================
#   10845번:    큐
#   @date:   2026-02-05
#   @link:   https://www.acmicpc.net/problem/10845
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
que = deque()
for _ in range(N):
    S = input()
    if "push" in S:
        A, B = S.split()
        que.append(B)
    elif "pop" in S:
        if len(que) == 0:
            print(-1)
        else:
            A = que.popleft()
            print(A)
    elif "size" in S:
        print(len(que))
    elif "empty" in S:
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif "front" in S:
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif "back" in S:
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
