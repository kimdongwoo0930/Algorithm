# =====================================================================
#   2775번:    부녀회장이 될테야
#   @date:   2026-01-30
#   @link:   https://www.acmicpc.net/problem/2775
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
# =====================================================================

import sys

input = sys.stdin.readline

N = int(input())
for j in range(N):
    k = int(input())
    n = int(input())
    room = [[]]
    for peo in range(1, n + 1):
        room[0].append(peo)
    for i in range(1, k + 1):
        room.append([])
        for m in range(n):
            room[i].append(sum(room[i - 1][: m + 1]))
    print(room[k][n - 1])
