#=====================================================================
#   2667번:    단지번호붙이기                   
#   @date:   2026-01-27              
#   @link:   https://www.acmicpc.net/problem/2667  
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================


'''
아이디어
    - 2중 for, 값이 1 and 방문 X => DFS 시작
    - DFS 통해서 찾은값 저장 후 출력

시간복잡도
    - DFS : O(V+E)
    - V, E : N ^ 2, 4N^2
    - V+E : 5N ^2 = 625

자료구조
    - 그래프 : int[][]
    - 방문여부 : bool[][]
    - 결과 : int[]
'''

import sys;

input = sys.stdin.readline


N = int(input())
graph = [list(map(int,input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []


dy = [1,0,-1,0]
dx = [0,1,0,-1]


def DFS(y,x):
    global each
    each += 1 
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<= ny < N and 0<= nx < N:
            if graph[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                DFS(ny,nx)



for j in range(N):
    for i in range(N):
        if graph[j][i] == 1 and chk[j][i] == False:
            # 방문여부 체크
            chk[j][i] = True
            each = 0
            # DFS 로 크기 구하기
            DFS(j,i)
            result.append(each)
            # 크기를 결과값에 넣기

result.sort()
print(len(result))
for i in result:
    print(i)

