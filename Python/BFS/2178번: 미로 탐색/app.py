#=====================================================================
#   2178번:    미로 탐색                   
#   @date:   2026-01-27              
#   @link:   https://www.acmicpc.net/problem/2178  
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

'''
아이디어:
    N x M 을 map함수만들기
    Map 1인지 아닌지 체크 and chk가 False인지 확인
    BFS로 탐색 후 가장 최소칸 대신 도착을 해야한다.

자료구조
    - 그래프 : int[][]
    - 방문여부 : bool[][]
    - BFS

'''



import sys;
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(N)]
chk = [[False] * M for _ in range(N)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]


def BFS():
    q = deque([(0,0,1)])
    chk[0][0] = True
    while q:
        ey, ex, dist = q.popleft()
        if ey == N-1 and ex == M-1:
            return dist
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0<= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append((ny,nx, dist + 1))



print(BFS())