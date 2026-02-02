#=====================================================================
#   2665번:    미로만들기                   
#   @date:   2026-01-28              
#   @link:   https://www.acmicpc.net/problem/2665  
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

"""
아이디어:
    하연색은 그냥 지나가
    검은색은 1씩 더해
    매번 서로 만날때 부순횟수가 작은걸로 변경
    그럼 가장먼저 도착하는게 최소값이다.
    
자료구조:
    graph = int[][]
    visited = int[][]

    
"""

import sys;
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
min_break = [[N*N] * N for _ in range(N)]


cx = [0,1,0,-1]
cy = [1,0,-1,0]


def bfs():
    q = deque([(0,0,0)])

    while q:
        ey, ex, dist = q.popleft()

        if ey == N-1 and ex == N-1:
            return dist
    
        for i in range(4):
            ny = ey + cy[i]
            nx = ex + cx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if graph[ny][nx] == 1:
                    if dist < min_break[ny][nx]:  
                        # 하얀벽일때 그냥 지나가
                        # 대신 햐얀벽을 먼저 가봐야 하니까 큐 맨 앞에 넣는다
                        q.appendleft([ny,nx, dist])
                        min_break[ny][nx] = dist
                else:  
                        # 검은벽일때 부셔 dist + 1
                        # 검은색은 하얀색을 쭉 간다음 검사해도되니 큐 맨뒤에 넣는다
                    if min_break[ny][nx] > dist + 1:
                        min_break[ny][nx] = dist + 1
                        q.append([ny,nx,dist + 1])

            


print(bfs())