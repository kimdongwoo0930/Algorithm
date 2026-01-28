#=====================================================================
#   1926번:    그림                   
#   @date:   2026-01-27              
#   @link:   https://www.acmicpc.net/problem/1926  
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

"""
아이디어
BFS로 탐색하고 넓이를 각각 저장해서 가장 큰걸 출력하자
먼저 이중for문으로 1이 나올떄마다 bfs 시작
중복 체크해야함

시간 복잡도
V = m x n    -> 500 x 500
E = V x 4.   -> 4 x 250000
O(V + E) = 5V. -> 5 x 250000 = 1250000 < 2억

자료구조
- 그래프 : int[][]
- 방문 : bool[][]
- BFS
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def BFS(y, x):
    rs = 1
    q = deque([(y, x)])
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    rs += 1
                    q.append((ny, nx))

    return rs


cnt = 0
maxV = 0

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 전체 그림 갯수 + 1
            cnt += 1
            # BFS 그림 최대 크기 구하기
            maxV = max(maxV, BFS(j, i))
            # 최대값 갱신
print(cnt)
print(maxV)
