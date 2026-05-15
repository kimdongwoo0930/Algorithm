#=====================================================================
#   10250번:    ACM 호텔                   
#   @date:   2026-01-28              
#   @link:   https://www.acmicpc.net/problem/10250  
#   @Motd:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;
from collections import deque

input = sys.stdin.readline


N = int(input())
List = [list(map(int, input().split())) for _ in range(N)]

for i in List:
    y = i[0]
    x = i[1]
    num = i[2]
    cnt = 0

    rooms = [[False] * x for _ in range(y)]
    for j in range(x):
        for k in range(y):
            if cnt == num - 1 :
                if j+1 < 10:
                    print(str(k + 1) + "0"+ str(j+1))
                else:
                    print(str(k + 1) + str(j + 1))
            rooms[k][j] = True
            cnt += 1 
            

